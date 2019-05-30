var ba = require('bitcoinaverage');

var pub = 'your public key';
var secret = 'your secret key';

function reorder(orderbook, symbols){
  var bprices = Object.values(orderbook[symbols[0]].bids);
  sorted_bids = bprices.sort(function(a, b){
    return a.price >= b.price ? -1 : 1;
  });
  var aprices = Object.values(orderbook[symbols[0]].asks);
  sorted_asks = aprices.sort(function(a, b){
    return a.price < b.price ? -1 : 1;
  });
}

function connect_orderbook(exchange, symbols){
  var ws = ba.websocketClient(pub, secret);
  var BOOK = {};
  symbols.forEach(function(symbol){
    BOOK[symbol] = {
      'asks': [],
      'bids': []
    };
  });
  var symbol = '';
  ws.connectToOrderbookWebsocket(exchange, symbols, function(response){
    symbol = response.data.symbol;
    if(response.data.type === "snapshot"){
      console.log("Got snapshot for " + symbol + response.data.asks.length);
      console.log("Best ASK: ");
      console.log(response.data.asks[0]);
      console.log("Best BID: ");
      console.log(response.data.bids[0]);
      BOOK[symbol].asks = response.data.asks;
      BOOK[symbol].bids = response.data.bids;
    }else{
      console.log("Now updates " + response.data.updates.length + response.data.symbol);
      for (var i = 0; i < response.data.updates.length; i++){
        var item = response.data.updates[i];
        if(item.amount === 0){
          delete(BOOK[symbol][item.side][item.price]);
        }else{
          BOOK[symbol][item.side][item.price] = item;
        }
      }
    }
  }, function(err){
    console.log(err);
  });
  setInterval(function(){reorder(BOOK, symbols)}, 10000)
}
