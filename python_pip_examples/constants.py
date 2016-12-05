
from bitcoinaverage import RestfulClient

if __name__ == '__main__':
    secret_key = '' or input('Enter your secret key: ')
    public_key = '' or input('Enter your public key: ')

    restful_client = RestfulClient(secret_key, public_key)

    all_symbols = restful_client.all_symbols()
    print('all symbols:')
    print(all_symbols)

    symbols_local = restful_client.symbols_local()
    print('local symbols')
    print(symbols_local)

    symbols_global = restful_client.symbols_global()
    print('global symbols')
    print(symbols_global)


    exchange_rates_local = restful_client.exchange_rates_local()
    print('local exchange rates')
    print(exchange_rates_local)

    exchange_rates_global = restful_client.exchange_rates_global()
    print('global exchange rates')
    print(exchange_rates_global)


    server_time = restful_client.server_time()
    print('Server time')
    print(server_time)