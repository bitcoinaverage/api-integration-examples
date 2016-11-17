import hashlib
import hmac
import requests
import time

secret_key = 'enter your secret key'
public_key = 'enter your public key'
timestamp = int(time.time())
payload = '{}.{}'.format(timestamp, public_key)
hex_hash = hmac.new(secret_key.encode(), msg=payload.encode(), digestmod=hashlib.sha256).hexdigest()
signature = '{}.{}'.format(payload, hex_hash)

url = 'https://apiv2.bitcoinaverage.com/indices/global/ticker/BTCUSD'
headers = {'X-Signature': signature}
result = requests.get(url=url, headers=headers)
print(result.json())

