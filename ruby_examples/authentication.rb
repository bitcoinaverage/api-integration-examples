require 'openssl'
require 'date'
require 'open-uri'

secret_key = 'enter your secret key'
public_key = 'enter your public key'
timestamp = Time.now.to_i
payload = timestamp.to_s + "." + public_key
hex_hash = OpenSSL::HMAC.hexdigest('sha256', secret_key, payload)
signature = payload + '.' + hex_hash

ticker_url = 'https://apiv2.bitcoinaverage.com/indices/global/ticker/BTCUSD'
response = open(ticker_url, 'X-Signature' => signature).read
puts response