from bitcoinaverage import ExchangeWebsocketClient

if __name__ == '__main__':
    secret_key = '' or input('Enter your secret key: ')
    public_key = '' or input('Enter your public key: ')

    print('Connecting to the exchange websocket...')
    ws = ExchangeWebsocketClient(public_key, secret_key)
    ws.exchange_data('bitstamp')
