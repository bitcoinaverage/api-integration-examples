'''
Example how to subscribe to ticker websocket.
'''
import hashlib
import hmac
import requests
import time
from websocket import create_connection
import simplejson as json

public_key = 'your public key'

ticket_url = "https://apiv2.bitcoinaverage.com/websocket/get_ticket"
ticket_header = {"x-ba-key": public_key}
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