# BitcoinAverage API integration examples
Examples of how to integrate with our API in various langauges

## BitcoinAverage Packages

We have published our own npm and pip packages that do the heavy lifting for you (authentication, handling requests, remembering the full urls).


###  NodeJS NPM Package
Our npm package exposes both websocket and restful clients for connecting to our live API channels and making HTTP requests.

```bash
npm install bitcoinaverage
```
#### Setup
```javascript
const ba = require('bitcoinaverage');

var publicKey = "<your pub key>";
var secretKey = "<your secret key>"; 
var restClient = ba.restfulClient(publicKey, secretKey);
var websocketClient = ba.websocketClient(publicKey, secretKey);
```

#### Ticker data

```javascript
restClient.tickerGlobalPerSymbol("BTCUSD", function(response){
	console.log(response);
});
```
[Full response format in our docs](https://apiv2.bitcoinaverage.com/#ticker-data-per-symbol)

#### Exchange data
```javascript
restClient.allExchangeDataForSymbol('BTCUSD', function(response) {
    console.log(response);
});

restClient.perExchangeData('gdax', function(response) {
    console.log(response);
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

