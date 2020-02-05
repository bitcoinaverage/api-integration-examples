require 'openssl'
require 'date'
require 'open-uri'

public_key = 'enter your public key'

ticker_url = 'https://apiv2.bitcoinaverage.com/indices/global/ticker/BTCUSD'
response = open(ticker_url, 'x-ba-key' => public_key).read
puts response