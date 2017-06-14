const ba = require('bitcoinaverage');

var publicKey = 'yourPublicKey';
var secretKey = 'yourSecretKey';
var restClient = ba.restfulClient(publicKey, secretKey);

// Works only for Enterprise users
restClient.allExchangesData('BTC', 'USD', function(response) {
    console.log(response);
});

// Works only for Enterprise users
restClient.allExchangeDataForSymbol('BTCUSD', function(response) {
    console.log(response);
});

restClient.perExchangeData('gdax', function(response) {
    console.log(response);
});


restClient.exchangeCount(function(response) {
    console.log(response);
});

restClient.outlierExchanges(function(response) {
    console.log(response);
});

restClient.ignoredExchanges(function(response) {
    console.log(response);
});

restClient.inactiveExchanges(function(response) {
    console.log(response);
});

restClient.currencyWeights(function(response) {
    console.log(response);
});

restClient.exchangeWeights(function(response) {
    console.log(response);
});