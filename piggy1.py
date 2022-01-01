from urllib.request import urlopen
import json
from datetime import datetime as dt
import datetime


import ssl



def make_info_vector(coin, num_days, key):
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        # Legacy Python that doesn't verify HTTPS certificates by default
        pass
    else:
        # Handle target environment that doesn't support HTTPS verification
        ssl._create_default_https_context = _create_unverified_https_context

    api_key = '&api_key={' + str(key) + '}'

    today = dt.today()
    today = today.replace(hour=0, minute=0, second=0, microsecond=0)

    start_epoch = today.timestamp()
    start_ep_string = str(start_epoch)
    num_days_string = str(num_days)

    # structure:
    # https://min-api.cryptocompare.com/data/v2/histoday?fsym= + coin_dict[index]
    # + &tsym=USD&limit= + number per page (max is 2000) +
    # &toTs= + epoch timestamp for most recent dat (I think it started in 2014)}, use 1609459200 aka start of 2021,
    # and it runs in reverse from there
    # + &api_key={ + key + }
    # returns string, converts to json

    historical_url = 'https://min-api.cryptocompare.com/data/v2/histoday?fsym=' + coin + \
                     '&tsym=USD&limit=' + num_days_string + '&toTs=' + start_ep_string + api_key

    resp = urlopen(historical_url)

    dic = json.load(resp)

    data_dic = dic["Data"]["Data"]
    print(coin)

    csv_list = []
    header = ["Coin", "Date", "Total Change Difference", "High/Low Difference"]
    csv_list.append(header)
    for dictionary in data_dic:
        list_entry = []
        list_entry.append(coin)
        list_entry.append(datetime.datetime.fromtimestamp(dictionary["time"]))
        list_entry.append(dictionary["close"] - dictionary["open"])
        list_entry.append(dictionary["high"] - dictionary["low"])
        csv_list.append(list_entry)
    return csv_list