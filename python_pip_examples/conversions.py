from bitcoinaverage import RestfulClient

if __name__ == '__main__':
    secret_key = '' or input('Enter your secret key: ')
    public_key = '' or input('Enter your public key: ')

    restful_client = RestfulClient(secret_key, public_key)

    # convert from BTC to USD
    conversion_local = restful_client.perform_conversion_local('BTC', 'USD', amount=3)
    print('3 BTC are worth {} USD'.format(conversion_local['price']))

    # convert from EUR to ETH
    conversion_global = restful_client.perform_conversion_global('EUR', 'ETH', amount=100)
    print('100 EUR are worth {} ETH'.format(conversion_global['price']))

    # get the price of BTCUSD when the transaction for the provided hash was confirmed
    blockchain_tx_price = restful_client.blockchain_tx_price('BTCUSD', 'f854aebae95150b379cc1187d848d58225f3c4157fe992bcd166f58bd5063449')
    print(blockchain_tx_price)