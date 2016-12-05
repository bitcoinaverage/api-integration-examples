from bitcoinaverage import RestfulClient

if __name__ == '__main__':
    secret_key = '' or input('Enter your secret key: ')
    public_key = '' or input('Enter your public key: ')

    restful_client = RestfulClient(secret_key, public_key)

    all_exchange_data = restful_client.all_exchange_data(crypto='BTC', fiat='USD,CNY')
    print('data from all exchanges for BTCUSD and BTCCNY')
    print(all_exchange_data)

    all_exchange_data_BTCUSD = restful_client.all_exchange_data_for_symbol('BTCUSD')
    print('data from all exchanges fro BTCUSD')
    print(all_exchange_data_BTCUSD)

    gdax_data = restful_client.per_exchange_data('gdax')
    print('data from GDAX')
    print(gdax_data)

    exchange_count = restful_client.exchange_count()
    print('exchange count')
    print(exchange_count)

    outlier_exchanges = restful_client.outlier_exchanges()
    print('outlier exchanges')
    print(outlier_exchanges)

    ignored_exchanges = restful_client.ignored_exchanges()
    print('ignored exchanges')
    print(ignored_exchanges)

    inactive_exchanges = restful_client.inactive_exchanges()
    print('inactive exchanges')
    print(inactive_exchanges)

    currency_weights = restful_client.currency_weights()
    print('currency weights')
    print(currency_weights)

    exchange_weights = restful_client.exchange_weights()
    print('exchange weights')
    print(exchange_weights)