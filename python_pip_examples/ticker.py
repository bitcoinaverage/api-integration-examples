from bitcoinaverage import RestfulClient


if __name__ == '__main__':
    secret_key = '' or input('Enter your secret key: ')
    public_key = '' or input('Enter your public key: ')

    restful_client = RestfulClient(secret_key, public_key)

    ticker_all_local = restful_client.ticker_all_local(crypto='LTC', fiat='GBP')
    print('ticker all local')
    print(ticker_all_local)

    ticker_all_global = restful_client.ticker_all_global(crypto='BTC', fiat='USD,EUR')
    print('ticker all global')
    print(ticker_all_global)

    ticker_local_per_symbol = restful_client.ticker_local_per_symbol('BTCUSD')
    print('Local Ticker for BTCUSD')
    print(ticker_local_per_symbol)

    ticker_global_per_symbol = restful_client.ticker_global_per_symbol('BTCUSD')
    print('Global Ticker for BTCUSD')
    print(ticker_global_per_symbol)

    ticker_short_local = restful_client.ticker_short_local()
    print('Local Ticker Short')
    print(ticker_short_local)

    ticker_short_global = restful_client.ticker_short_global()
    print('Global Ticker Short')
    print(ticker_short_global)

    print('Generate price index for BTCUSD based only on the data from Bitstamp and Kraken')
    ticker_custom_include = restful_client.ticker_custom_include('BTCUSD', 'bitstamp,kraken')
    print(ticker_custom_include)

    print('Generate price index for BTCUSD based on the data from all exchanges except Bitstamp and Kraken')
    ticker_custom_exclude = restful_client.ticker_custom_exclude('BTCUSD', 'bitstamp,kraken')
    print(ticker_custom_exclude)

    ticker_changes_all_local = restful_client.ticker_changes_all_local()
    print('Local Ticker values with changes')
    print(ticker_changes_all_local)

    ticker_changes_local_btcusd = restful_client.ticker_changes_local('BTCUSD')
    print('Ticker including changes (for BTCUSD):')
    print(ticker_changes_local_btcusd)

    ticker_changes_global_btceur = restful_client.ticker_changes_global('BTCEUR')
    print('Ticker including changes (for BTCEUR):')
    print(ticker_changes_global_btceur)