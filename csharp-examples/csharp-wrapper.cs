using Newtonsoft.Json.Linq;
using System;
using System.Net.Http;
using System.Net.WebSockets;
using System.Security.Cryptography;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

//https://apiv2.bitcoinaverage.com/
namespace InvestAgg.Server.BitcoinAverage
{
    /// <summary>
    /// Asynchronous wrapper for the V2 API at bitcoinaverage.
    /// Written by Fredrik Nøring at Norkon Computing Systems
    /// </summary>
    public class BitcoinAverageApi
    {
        public const string BITCOIN_TICKER = "BTCUSD";
        public const string GLOBAL_MARKET = "global";

        private readonly string _publicKey;
        private readonly string _secretKey;
        private readonly HMACSHA256 _sigHasher;
        private readonly DateTime _epochUtc = new DateTime(1970, 1, 1, 0, 0, 0, DateTimeKind.Utc);

        public BitcoinAverageApi(string publicKey, string secretKey)
        {
            _secretKey = secretKey;
            _publicKey = publicKey;
            _sigHasher = new HMACSHA256(Encoding.ASCII.GetBytes(_secretKey));
        }

        public string GetHeaderSignature()
        {
            var timestamp = (int)((DateTime.UtcNow - _epochUtc).TotalSeconds);
            var payload = timestamp + "." + _publicKey;
            var digestValueBytes = _sigHasher.ComputeHash(Encoding.ASCII.GetBytes(payload));
            var digestValueHex = BitConverter.ToString(digestValueBytes).Replace("-", "").ToLower();
            return payload + "." + digestValueHex;
        }

        public async Task<JToken> GetJsonAsync(string url)
        {
            using (var httpClient = new HttpClient())
            {
                httpClient.DefaultRequestHeaders.Add("X-signature", GetHeaderSignature());
                return JToken.Parse(await httpClient.GetStringAsync(url));
            }
        }

        public Task<JToken> GetBitcoinAllTimeHistoricalDataAsync() => GetAllTimeHistoricalDataAsync(BITCOIN_TICKER);

        public Task<JToken> GetAllTimeHistoricalDataAsync(string symbol, string market = GLOBAL_MARKET)
        {
            var url = "https://apiv2.bitcoinaverage.com/indices/" + market + "/history/" + symbol + "?"
                   + "&period=alltime"
                   + "&format=json";

            return GetJsonAsync(url);
        }

        public Task<JToken> GetBitcoinDailyDataAsync() => GetDailyDataAsync(BITCOIN_TICKER);

        public Task<JToken> GetDailyDataAsync(string symbol, string market = GLOBAL_MARKET)
        {
            var url = "https://apiv2.bitcoinaverage.com/indices/" + market + "/history/" + symbol + "?"
                   + "&period=daily"
                   + "&format=json";

            return GetJsonAsync(url);
        }

        public Task<JToken> GetBitcoinOhlcAsync() => GetOhlcAsync(BITCOIN_TICKER);

        public Task<JToken> GetOhlcAsync(string symbol, string market = GLOBAL_MARKET)
        {
            var url = "https://apiv2.bitcoinaverage.com/indices/" + market + "/ticker/" + symbol;
            return GetJsonAsync(url);
        }

        public async Task<string> GetWebsocketTicket()
        {
            var url = "https://apiv2.bitcoinaverage.com/websocket/get_ticket";
            var jToken = await GetJsonAsync(url);
            return jToken["ticket"].Value<string>();
        }

        public Task StartBitcoinStreaming(CancellationToken ct, Action<JToken> notifier)
        {
            var subscriptionMessage = new JObject
            {
                { "event", "message" },
                { "data", new JObject
                    {
                        { "operation", "subscribe" },
                        { "options", new JObject
                            {
                                {  "market", "global" },
                                { "currency", BITCOIN_TICKER }
                            }
                        }
                    }
                }
            };

            return StartWebsocketStreaming(ct, notifier, subscriptionMessage);
        }

        public async Task StartWebsocketStreaming(CancellationToken ct, Action<JToken> notifier, JObject subscribeMessage)
        {
            var buffer = new byte[1048576]; //1MB
            var str = subscribeMessage.ToString(Newtonsoft.Json.Formatting.None);

            var ticket = await GetWebsocketTicket();
            var url = "wss://apiv2.bitcoinaverage.com/websocket/ticker?public_key=" + _publicKey + "&ticket=" + ticket;

            using (var webSocket = new ClientWebSocket())
            {
                await webSocket.ConnectAsync(new Uri(url), ct);

                //Send the subscribe message
                var subscribeArraySegment = new ArraySegment<byte>(buffer, 0, Encoding.UTF8.GetBytes(str, 0, str.Length, buffer, 0));
                await webSocket.SendAsync(subscribeArraySegment, WebSocketMessageType.Text, true, ct);

                while (true)
                {
                    ct.ThrowIfCancellationRequested();
                    notifier(await ReceiveNextWebsocketString(webSocket, buffer, ct));
                }
            }
        }

        private async Task<string> ReceiveNextWebsocketString(ClientWebSocket webSocket, byte[] buffer, CancellationToken ct)
        {
            var index = 0;

            while (true)
            {
                var receiveResult = await webSocket.ReceiveAsync(new ArraySegment<byte>(buffer, index, buffer.Length - index), ct);

                if (receiveResult.CloseStatus.HasValue)
                    return null;

                index += receiveResult.Count;

                if (!receiveResult.EndOfMessage)
                    continue;

                return Encoding.UTF8.GetString(buffer, 0, index);
            }
        }
    }
}
