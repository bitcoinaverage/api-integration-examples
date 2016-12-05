from bitcoinaverage import RestfulClient
from datetime import datetime, timedelta

if __name__ == '__main__':
    secret_key = '' or input('Enter your secret key: ')
    public_key = '' or input('Enter your public key: ')

    restful_client = RestfulClient(secret_key, public_key)

    # load local history as dict
    history_local_json = restful_client.history_local('BTCUSD', 'daily', 'json')

    # save history in history_local.csv
    restful_client.save_history_local(symbol='BTCUSD', period='daily', csv_path='history_local.csv')

    # load global history as dict
    history_global_json = restful_client.history_global('BTCUSD', 'daily', 'json')

    # save history in history_global.csv format
    restful_client.save_history_global(symbol='LTCEUR', period='alltime', csv_path='history_global.csv')

    # get unix format timestamp for 10 minutes ago
    timestamp = int((datetime.now() - timedelta(minutes=10)).timestamp())
    # get all local history data since the specified timestamp (for the last 10 minutes)
    data_since_timestamp = restful_client.data_since_timestamp_local('BTCUSD', since=timestamp)
    print('local data for the last 10 minutes (since {} timestamp)'.format(timestamp))
    print(data_since_timestamp)

    timestamp = int((datetime.now() - timedelta(minutes=10)).timestamp())
    # get all global history data since the specified timestamp (for the last 10 minutes)
    data_since_timestamp = restful_client.data_since_timestamp_global('BTCUSD', since=timestamp)
    print('global data for the last 10 minutes (since {} timestamp)'.format(timestamp))
    print(data_since_timestamp)

    timestamp = int((datetime.now() - timedelta(minutes=10)).timestamp())
    # get the global price at the moment closest to the specified timestamp
    price_at_timestamp_global = restful_client.price_at_timestamp_global('BTCEUR', timestamp)
    print('price at timestamp global')
    print(price_at_timestamp_global)