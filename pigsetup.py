import piggy1
import csv


def setup(coin_list, day_range, key):
    # assumes that each coin has existed since start of 2021
    check_coins = ['BTC', 'BTT', 'ETH', 'AVAX', 'SOL', 'TRX', 'BNB', 'LUNA', 'XRP', 'USDT',
                   'FTM, CRV, TRN', 'BUSD, DOT', 'BTT', 'MATIC', 'SHIB', 'SAND', 'LINK',
                   'FARM', 'YFI', 'LTC', 'DOGE', 'BCH', 'MANA', 'XLM', 'FIL', 'BAT', 'ICP',
                   'LRP', 'KAVA', 'VET', 'ENJ', 'MIOTA', 'ETC', 'GRT', 'SYS', 'QTUM']

    #full error check before running anything -- not very efficient
    for coin in coin_list:
        if coin not in check_coins:
            return -1


    int_day = int(day_range) #make sure it's an integer
    if int_day < 0 or int_day > 1000:
        return -1

    #no errors, run the api call
    blank_row = ['', '', '', '']
    with open('piggybank_results.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for coin in coin_list:
            csv_list = piggy1.make_info_vector(coin, day_range, key)
            writer.writerow(csv_list[0]);
            for i in range(1, int_day + 1):
                writer.writerow(csv_list[i])
            writer.writerow(blank_row)
    return 0