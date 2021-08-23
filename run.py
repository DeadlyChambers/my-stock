#!/usr/bin/python
import getopt
import json
import sys

import stock_plot as plot
import stock_profile as sp


def main(argv):
    input_file = 'stocks.json'
    interval = 'monthly'
    usage = 'Error occurred, ensure you are calling the function as \n' \
            'run.py [-h] [-s|--show] [-i|--interval (monthly|daily|yearly|five)] [-c|--columns (3)]'
    columns = 3
    try:
        opts, args = getopt.getopt(argv, "hi:c:", ["interval=", "columns="])
    except getopt.GetoptError:
        print(usage)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(usage)
            sys.exit()
        elif opt in ("-i", "--interval"):
            interval = arg
        elif opt in ("-c", "--columns"):
            columns = int(arg)
        else:
            print(f'arg {arg} not recognized')
            print(usage)
            sys.exit()

    f = open(input_file, )
    data = json.load(f)
    stocks = []
    for rec in data['data']:
        stocks.append(sp.StockProfile(rec['name'], rec['cost'], rec['total'], interval=interval))
    plot.get(stocks, columns=columns)
    f.close()


if __name__ == "__main__":
    main(sys.argv[1:])
