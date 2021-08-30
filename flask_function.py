import stock_plot as plot
import stock_profile as sp
import json
from flask_cors import CORS
from flask import Flask, request, make_response


app = Flask(__name__)
CORS(app) #Prevents CORS errors 

@app.route('/', methods=('GET',))
def get_handler():
    """Get Handler
    :Parameters:
        Just a simple get method to test the plot functionality
    """
    input_file = 'stocks.json'
    interval = 'monthly'
    f = open(input_file, )
    data = json.load(f)
    stocks = []
    for rec in data['data']:
        stocks.append(sp.StockProfile(rec['name'], rec['cost'], rec['total'], interval=interval))
    stock_output = plot.get(stocks, columns=3)
    f.close()
    return {
        'StatusCode': 200,
        'ContentType': 'text/html',
        'Content': stock_output
    }


@app.route('/', methods=('POST',))
def request_handler():
    """Get Handler
    :Parameters:
        Just a simple POST method that will enable my other api to retrieve the
        graphs
    """
    event = request.get_json()
    interval = event['interval']
    columns = int(event['columns'])
    stocks = []
    print(f'Interval of {interval}')
    for rec in event['data']:
        stocks.append(sp.StockProfile(rec['name'], rec['cost'], rec['total'],
                                      interval=interval))
    stock_output = plot.get(stocks, columns=columns)
    return {
        'StatusCode': 200,
        'ContentType': 'text/html',
        'Content': stock_output
    }


if __name__ == "__main__":
    get_handler()
