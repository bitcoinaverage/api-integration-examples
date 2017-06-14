const ba = require('bitcoinaverage');

var publicKey = 'yourPublicKey';
var secretKey = 'yourSecretKey';
var restClient = ba.restfulClient(publicKey, secretKey);

// Convert from ETH to USD
var from = 'ETH', to = 'USD', amount = 3;
restClient.performConversionLocal(from, to, amount, function (response) {
    response = JSON.parse(response);
    console.log("At time " + response.time + " the cost of " + amount + " " + from + " is " + response.price + " " + to);
});

// Convert EUR to LTC
var fromFiat = 'EUR', toCrypto = 'LTC';
restClient.performConversionLocal(fromFiat, toCrypto, amount, function (response) {
    response = JSON.parse(response);
    console.log("At time " + response.time + " the cost of " + amount + " " + fromFiat + " is " + response.price + " " + toCrypto);
});

// Get price when given hash was mined
var hash = 'f854aebae95150b379cc1187d848d58225f3c4157fe992bcd166f58bd5063449';
restClient.blockchainTxPrice('BTCUSD', hash, function (response) {
    response = JSON.parse(response);
    console.log("1 BTC was worth " + response.average + " when the transaction of the hash " + hash + " was conducted");
});