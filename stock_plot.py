# Raw Package
from datetime import date
from re import template
import numpy as np
import pandas as pd
from plotly.subplots import make_subplots
import stock_profile as model

#Data Source
import yfinance as yf

#Data viz
import plotly.graph_objs as go
total_assets=0
net_gains=0
interval = "monthly"
start_date=date.today
end_date=date.today

def set_data(stockProfile):
    #Interval required 1 minute
    stockProfile.data = yf.download(tickers=stockProfile.name, period=stockProfile.period, interval=stockProfile.interval)
    stockProfile.set_current(stockProfile.data.values.item(stockProfile.data.values.size-2))
    global total_assets, net_gains
    net_gains += stockProfile.net_value
    total_assets += stockProfile.current_value
   
def get(stocks):
    [set_data(stock) for stock in stocks]
    
    #declare figure
    fig = make_subplots(
        rows=4, cols=3, #loop array
        #subplot_titles=[stock.to_string() for stock in stocks],
        y_title='', #y_title_font_color=stock.color_text
    )
    row=1
    col=1
    for stock in stocks:
        #Candlestick
        if col == 4:
            col=1
            row+=1
        #fig.add_trace(go.Candlestick(x=stock.data.index,        
                        # open=stock.data['Open'],
                        # high=stock.data['High'],
                        # low=stock.data['Low'],
                        # close=stock.data['Close'], name=stock.name), row=row, col=col)
        fig.add_trace(go.Scatter(x=stock.data.index, y=stock.data['Close'], 
                        mode='lines', connectgaps=True,
                        line=dict(color=stock.color_text),
                        # open=stock.data['Open'],
                        # high=stock.data['High'],
                        # low=stock.data['Low'],
                        # close=stock.data['Close'],
                        name=f'{stock.name}<br><span style="color:{stock.color_text}">{stock.result}</span>'), row=row, col=col)
        col+=1
    row=1
    col=1
    count=0
    backgrounds = []
    for stock in stocks:
        #Candlestick
        if col == 4:
            col=1
            row+=1
        fig.update_xaxes(title_text=stock.to_string(), row=row,col=col, rangeslider_visible=False, title_font_color=stock.color_text, title_font_size=12)
        fig.update_yaxes(title_text=stock.name, row=row,col=col, title_font_color="black")
        cur_plot = fig.data[count]
        sd = stock.data;
        global start_date, end_date
        start_date = cur_plot.x[0]
        end_date = cur_plot.x[len(cur_plot.x)-1]
        backgrounds.append(dict(type="rect",
            xref=cur_plot.xaxis,yref=cur_plot.yaxis,
            x0=int(start_date.timestamp()*1000),x1=int(end_date.timestamp()*1000),
            y0=min(sd.Low.values),y1=max(sd.High.values),name=f"hey-{count}",
            fillcolor=stock.color_bg,opacity=0.25,layer="above",
            line_width=0))
        count+=1        
        col+=1
        
    fig.update_layout(title_text=f'<b style="font-size:20px;">My Stock Portfolio</b> - <b>Total:</b> {total_assets} | <b>Net:</b> {round(net_gains,2)} - {interval} interval {start_date}  {end_date}', 
    height=1400, font=dict(size=12), shapes=backgrounds)

    #Show
    fig.show()

stocks = [ model.StockProfile("CLF", 21.50, 223, interval), model.StockProfile("DNN", 1.05, 276, interval), 
model.StockProfile("BB", 14.93, 40, interval), model.StockProfile("LEU", 23.75, 10, interval), 
model.StockProfile("LAC", 14.75, 16, interval), model.StockProfile("TBPMF", .27, 1250, interval), 
model.StockProfile("DAL", 47.5, 19, interval), model.StockProfile("NCLH", 99.66, 4, interval), model.StockProfile("TRU", 88.63, 203.981, interval), model.StockProfile("AVIR",33.4,11, interval)]
get(stocks)