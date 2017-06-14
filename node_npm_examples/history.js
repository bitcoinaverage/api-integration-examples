const ba = require('bitcoinaverage');

var publicKey = 'yourPublicKey';
var secretKey = 'yourSecretKey';
var restClient = ba.restfulClient(publicKey, secretKey);

restClient.historyLocal('BTCUSD', 'daily', function(response) {
    console.log(response);
});

restClient.historyGlobal('BTCUSD', 'daily', function (response) {
    console.log(response);
});


// Getting the Unix timestamp for the moment in time 10 minutes ago from now
var now = new Date();
var minutesAgo = 10;
var tenMinutesAgo = new Date(now.getTime() - minutesAgo * 60000);
var timestamp = parseInt(tenMinutesAgo.getTime() / 1000);

// Get local history for last 10 minutes
restClient.dataSinceTimestampLocal('BTCUSD', timestamp, function (response) {
    console.log(response);
});

// Get global history for last 10 minutes
restClient.dataSinceTimestampGlobal('BTCUSD', timestamp, function (response) {
    console.log(response);
});

// Get the local price at the moment closest to the specified timestamp
restClient.priceAtTimestampLocal('BTCEUR', timestamp, function (response) {
    console.log(response);
});

// Get the global price at the moment closest to the specified timestamp
restClient.priceAtTimestampGlobal('BTCEUR', timestamp, function (response) {
    console.log(response);
});

