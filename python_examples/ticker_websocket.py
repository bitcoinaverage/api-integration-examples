'''
Example how to subscribe to ticker websocket.
'''
import hashlib
import hmac
import requests
import time
from websocket import create_connection
import simplejson as json

secret_key = 'your secret key'
public_key = 'your public key'
timestamp = int(time.time())
payload = '{}.{}'.format(timestamp, public_key)
hex_hash = hmac.new(secret_key.encode(), msg=payload.encode(), digestmod=hashlib.sha256).hexdigest()
signature = '{}.{}'.format(payload, hex_hash)

ticket_url = "https://apiv2.bitcoinaverage.com/websocket/get_ticket"
ticket_header = {"X-signature": signature}
ticket = requests.get(url=ticket_url, headers=ticket_header).json()["ticket"]

url = "wss://apiv2.bitcoinaverage.com/websocket/ticker?public_key={}&ticket={}".format(public_key, ticket)
ws = create_connection(url)

# Here the values for currency and market may be changed.
# Market is either local or global.
subscribe_message = json.dumps({"event": "message",
                                "data": {
                                    "operation": "subscribe",
                                    "options": {
                                        "currency": "BTCUSD",
                                        "market": "local"
                                    }
                                }
                                })

ws.send(subscribe_message)

while True:
    result = ws.recv()
    print("Received '%s'" % result)