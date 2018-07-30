# BitcoinAverage API integration examples
Examples of how to integrate with our API in various langauges

## BitcoinAverage Packages

We have published our own npm and pip packages that do the heavy lifting for you (authentication, handling requests, remembering the full urls).

### NPM Package
This library enables quick and easy access to our Bitcoin, Ethereum, Litecoin, Ripple and other cryptocurrency exchange rates.

### Install


```
npm install bitcoinaverage
```


### Setup
Get your public and private keys from our website and you are ready to run these examples.

```javascript
const ba = require('bitcoinaverage');

var publicKey = 'yourPublicKey';
var secretKey = 'yourSecretKey';

var restClient = ba.restfulClient(publicKey, secretKey);
var wsClient = ba.websocketClient(publicKey, secretKey);
```



### Ticker Data
The response received by https://apiv2.bitcoinaverage.com/indices/global/ticker/BTCUSD.

The symbol_set can be one of: local, global, crypto and tokens.

The symbol can be any pair from our [Full symbol list](https://apiv2.bitcoinaverage.com/constants/indices/ticker/symbols)
```javascript
var symbol_set = 'global';
var symbol = 'BTCUSD';

restClient.getTickerDataPerSymbol('global', 'BTCUSD', function(response) {
    console.log(response);
}, function(error){
    console.log(error);
}) ;
```

### Exchange Data

#### All price data from single exchange
```javascript
restClient.perExchangeData('bitstamp',
    function(response){
        console.log(response);
    },
    function(err){
        console.log(err);
    });
```

#### Data from all exchanges for one symbol
```javascript
restClient.allExchangeDataForSymbol('BTCGBP',
    function(response){
        console.log(response);
    },
    function(err){
        console.log(err);
    });
```

### Websocket
Connect to one of our websocket endpoints and get real-time updates for the Bitcoin Global Price Index.

#### Ticker websocket

```javascript
wsClient.connectToTickerWebsocket('global', 'BTCUSD', function(response) {
    console.log(response);
}, function(error){
    console.log(error)
}, function(){
    console.log("websocket closed");
});
```

#### Orderbook websocket

The orderbook channel starts by sending a "snapshot" message with the current state of the orderbook.
Then it is followed by "update" messages that represent the changes in the orderbook.

If the amount for an order is 0, the order has been completed, so it needs to be removed from the orderbook.

If the amount is greater than 0 then we just update value.
```javascript
var symbols = ['BTCUSD', 'ETHUSD'];
var exchange = 'bitfinex';
var ORDERBOOKS = {
    BTCUSD: {},
    ETHUSD: {}
};
var symbol = '';
wsClient.connectToOrderbookWebsocket(exchange, symbols, function(response){
    symbol = respnose.data.symbol;
    if(response.data.type === "snapshot"){
        ORDERBOOKS[symbol].asks = response.data.asks;
        ORDERBOOKS[symbol].bids = response.data.bids;
     }else{
       console.log(response.data.updates);
       for (var i = 0; i < response.data.updates.length; i++){
          var item = response.data.updates[i];
         if(item.amount === 0){
            delete(ORDERBOOKS[symbol][item.side][item.price]);
         }else{
           ORDERBOOKS[symbol][item.side][item.price] = item;
         }
       }
     }
}, function(err){
console.log(err);
});
```

### Python PIP Package


```bash
pip install bitcoinaverage
```

#### Setup
```python
from bitcoinaverage import RestfulClient
restful_client = RestfulClient("<secret key>", "<public key>")
```

#### Ticker data
```python
ticker_global = restful_client.ticker_all_global(crypto="ETH", fiat="USD,EUR")
print(ticker_global)
```

#### Exchange data
```python
all_bitstamp_data = restful_client.per_exchange_data('bitstamp')
all_coinbase_data = restful_client.per_exchange_data('gdax')

all_exchange_data_gbp_brl = restful_client.all_exchange_data(crypto='BTC', fiat='GBP,BRL')
```

