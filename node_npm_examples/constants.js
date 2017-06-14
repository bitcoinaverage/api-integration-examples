const ba = require('bitcoinaverage');

var publicKey = 'yourPublicKey';
var secretKey = 'yourSecretKey';
var restClient = ba.restfulClient(publicKey, secretKey);

restClient.allSymbols(function (response) {
    console.log(response);
});

restClient.symbolsLocal(function (response) {
    console.log(response);
});

restClient.symbolsGlobal(function(response) {
    console.log(response);
});

restClient.exchangeRatesLocal(function(response) {
    console.log(response);
});

restClient.exchangeRatesGlobal(function(response) {
    console.log(response);
});

restClient.serverTime(function(response) {
    console.log(response);
});