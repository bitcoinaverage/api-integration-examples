import hashlib
import hmac
import requests
import time

public_key = 'enter your public key'
url = 'https://apiv2.bitcoinaverage.com/indices/global/ticker/BTCUSD'
headers = {'x-ba-key': public_key}
result = requests.get(url=url, headers=headers)
print(result.json())

