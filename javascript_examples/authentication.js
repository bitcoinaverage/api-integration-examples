/**
 * npm install -g crypto-js
 * npm install -g request
 */

var crypto = require('crypto-js');

var public_key = 'enter your public key';
var ticker_btcusd_url = 'https://apiv2.bitcoinaverage.com/indices/global/ticker/BTCUSD';

var request = require('request');
var options = {
    url: ticker_btcusd_url,
    headers: {
        'x-ba-key': public_key
    }
};
function callback(error, response, body) {
    if (!error && response.statusCode === 200) {
        console.log(body);
    }
}

request(options, callback);

