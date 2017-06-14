const ba = require('bitcoinaverage');

var publicKey = 'yourPublicKey';
var secretKey = 'yourSecretKey';
var ws = ba.websocketClient(publicKey, secretKey);

// Connecting to the Exchange websocket and printing Bitstamp data
ws.connectToExchangeWebsocket('bitstamp', function (response) {
    console.log(JSON.stringify(response, null, 4));
});
