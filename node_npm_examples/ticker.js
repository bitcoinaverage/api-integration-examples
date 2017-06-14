const ba = require('bitcoinaverage');

var publicKey = 'yourPublicKey';
var secretKey = 'yourSecretKey';
var restClient = ba.restfulClient(publicKey, secretKey);

// Get local ticker for BTCUSD and ETHUSD
restClient.tickerAllLocal('BTC,ETH', 'USD', function (response) {
    console.log(response);
});

// Get global ticker for BTCUSD and BTCEUR
restClient.tickerAllGlobal('BTC', 'USD,EUR', function(response) {
    console.log(response);
});

// Get local ticker for BTCUSD
restClient.tickerLocalPerSymbol('BTCUSD', function (response) {
    console.log(response);
});

// Get global ticker for BTCGBP
restClient.tickerGlobalPerSymbol('BTCGBP', function (response) {
    console.log(response);
});


// 4 examples for short ticker using the local market:
// 1. Get local short ticker for BTCUSD and BTCEUR
restClient.tickerShortLocal('BTC', 'USD,EUR', function (response) {
    console.log(response);
});

// 2. Get local short ticker for BTC and all supported fiat currencies
restClient.tickerShortLocal('BTC', '', function (response) {
    console.log(response);
});

// 3. Get local short ticker for all crypto currencies, represented in USD
restClient.tickerShortLocal('', 'USD', function (response) {
    console.log(response);
});

// 4. Get local short ticker for all available crypto-fiat pairs
restClient.tickerShortLocal('', '', function (response) {
    console.log(response);
});


// 4 examples for short ticker using the global market:
// 1. Get global short ticker for BTCUSD and BTCEUR
restClient.tickerShortGlobal('BTC', 'USD,EUR', function (response) {
    console.log(response);
});

// 2. Get global short ticker for BTC and all supported fiat currencies
restClient.tickerShortGlobal('BTC', '', function (response) {
    console.log(response);
});

// 3. Get global short ticker for all crypto currencies, represented in USD
restClient.tickerShortGlobal('', 'USD', function (response) {
    console.log(response);
});

// 4. Get global short ticker for all available crypto-fiat pairs
restClient.tickerShortGlobal('', '', function (response) {
    console.log(response);
});

// Custom ticker
// Generate price index for BTCUSD based only on the data from Bitstamp and Kraken
restClient.tickerCustomInclude('BTCUSD', 'bitstamp,kraken', function (response) {
    console.log(response);
});

// Generate price index for BTCUSD based on the data from all exchanges except Bitstamp and Kraken
restClient.tickerCustomExclude('BTCUSD', 'bitstamp,kraken', function (response) {
    console.log(response);
});

// Get ticker and changes for all supported symbols
restClient.tickerChangesAllLocal(function(response) {
    console.log(response);
});

// Get Local Ticker and changes only for BTCUSD
restClient.tickerChangesLocal('BTCUSD', function (response) {
    console.log(response);
});

// Get Global Ticker and changes only for ETHUSD
restClient.tickerChangesGlobal('ETHUSD', function (response) {
    console.log(response);
});