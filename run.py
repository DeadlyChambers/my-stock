#!/usr/bin/python
import getopt
import json
import sys

import stock_plot as plot
import stock_profile as sp




def main(argv):
    output_file = "index.html"
    input_file = 'stocks.json'
    interval = 'monthly'
    try:
        opts, args = getopt.getopt(argv, "hsi:", ["show=", "interval="])
    except getopt.GetoptError:
        print('run.py -s')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -s')
            sys.exit()
        elif opt in ("-s", "--show"):
            output_file = ""
        elif opt in ("-i", "--interval"):
            interval = arg

    f = open(input_file, )
    data = json.load(f)
    stocks = []
    for rec in data['data']:
        stocks.append(sp.StockProfile(rec['name'], rec['cost'], rec['total'], interval=interval))
    plot.get(stocks, output_file=output_file)
    f.close()


if __name__ == "__main__":
    main(sys.argv[1:])
