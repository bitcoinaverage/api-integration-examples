const ba = require('bitcoinaverage');

var publicKey = 'yourPublicKey';
var secretKey = 'yourSecretKey';
var ws = ba.websocketClient(publicKey, secretKey);

// Connecting to the local ticker and printing BTCEUR price data; you can try it with 'global'
ws.connectToTickerWebsocket('local', 'BTCEUR', function (response) {
    console.log(JSON.stringify(response, null, 4));
});