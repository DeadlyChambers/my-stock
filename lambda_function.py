import stock_plot as plot
import stock_profile as sp


def lambda_function(event, context):
    interval = event['interval']
    columns = int(event['columns'])
    stocks = []
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
    lambda_function("", "")
