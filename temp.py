# Raw Package
from datetime import date
from plotly.subplots import make_subplots
import stock_profile as model
import math

# Data Source
import yfinance as yf

# Data viz
import plotly.graph_objs as go

total_assets = 0
net_gains = 0
interval = "monthly"
start_date = date.today
end_date = date.today


def set_data(stock_profile):
    # Interval required 1 minute
    stock_profile.data = yf.download(tickers=stock_profile.name, period=stock_profile.period,
                                     interval=stock_profile.interval)
    stock_profile.set_current(stock_profile.data.values.item(stock_profile.data.values.size - 2))
    global total_assets, net_gains
    net_gains += stock_profile.net_value
    total_assets += stock_profile.current_value


def get(my_stocks):
    # declare figure
    fig = make_subplots(
        rows=math.floor(len(my_stocks)), cols=3,  # loop array
        # subplot_titles=[stock.to_string() for stock in stocks],
        y_title='',  # y_title_font_color=stock.color_text
    )
    for count, stock in enumerate(my_stocks, start=1):
        row = math.ceil(count / 3)
        col = count - ((row - 1) * 3)
        # fig.add_trace(go.Candlestick(x=stock.data.index,
        # open=stock.data['Open'],
        # high=stock.data['High'],
        # low=stock.data['Low'],
        # close=stock.data['Close'], name=stock.name), row=row, col=col)
        set_data(stock)
        fig.add_trace(go.Scatter(x=stock.data.index, y=stock.data['Close'],
                                 mode='lines', connectgaps=True,
                                 line=dict(color=stock.color_text),
                                 # open=stock.data['Open'],
                                 # high=stock.data['High'],
                                 # low=stock.data['Low'],
                                 # close=stock.data['Close'],
                                 name=f'{stock.name}<br><span style="color:{stock.color_text}">{stock.result}</span>'),
                      row=row, col=col)
    backgrounds = []
    for count, stock in enumerate(my_stocks, start=1):
        row = math.ceil(count / 3)
        col = count - ((row - 1) * 3)
        # Style the X and Y axes for each individual subplot
        fig.update_xaxes(title_text=stock.to_string(), row=row, col=col, rangeslider_visible=False,
                         title_font_color=stock.color_text, title_font_size=12)
        fig.update_yaxes(title_text=stock.name, row=row, col=col, title_font_color="black")
        cur_plot = fig.data[count -1]
        sd = stock.data
        global start_date, end_date
        start_date = cur_plot.x[0]
        end_date = cur_plot.x[len(cur_plot.x) - 1]
        # Add the colored shape to each subplot depending on net positive or negative
        backgrounds.append(dict(type="rect",
                                xref=cur_plot.xaxis, yref=cur_plot.yaxis,
                                x0=int(start_date.timestamp() * 1000), x1=int(end_date.timestamp() * 1000),
                                y0=min(sd.Low.values), y1=max(sd.High.values), name=f"{stock.name}",
                                fillcolor=stock.color_bg, opacity=0.25, layer="above",
                                line_width=0))

    fig.update_layout(
        title_text=f'<b style="font-size:20px;">My Stock Portfolio</b> - <b>Total:</b> {total_assets} | '
                   f'<b>Net:</b> {round(net_gains, 2)} - {interval} interval {start_date}  {end_date}',
        height=1400, font=dict(size=12), shapes=backgrounds)

    fig.show()


stocks = [model.StockProfile("CLF", 21.50, 223, interval), model.StockProfile("DNN", 1.05, 276, interval),
          model.StockProfile("BB", 14.93, 40, interval), model.StockProfile("LEU", 23.75, 10, interval),
          model.StockProfile("LAC", 14.75, 16, interval), model.StockProfile("TBPMF", .27, 1250, interval),
          model.StockProfile("DAL", 47.5, 19, interval), model.StockProfile("NCLH", 99.66, 4, interval),
          model.StockProfile("TRU", 88.63, 203.981, interval), model.StockProfile("AVIR", 33.4, 11, interval)]
get(stocks)
