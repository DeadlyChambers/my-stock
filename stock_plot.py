# Raw Package
import numpy as np
import pandas as pd
from plotly.subplots import make_subplots
from yachalk import chalk
import stock_profile as model

#Data Source
import yfinance as yf

#Data viz
import plotly.graph_objs as go

def set_data(stockProfile):
    #Interval required 1 minute
    stockProfile.data = yf.download(tickers=stockProfile.name, period='1d', interval='1m')
    stockProfile.set_current(stockProfile.data.values.item(stockProfile.data.values.size-2))
   
def get(stocks):
    [set_data(stock) for stock in stocks]
    
    #declare figure
    fig = make_subplots(
        rows=2, cols=4,
        subplot_titles= [stock.to_string() for stock in stocks],
        y_title='Stock Price (USD per Shares)',
    )
    row=1
    col=1
    for stock in stocks:
        #Candlestick
        if col == 5:
            col=1
            row+=1
        fig.add_trace(go.Candlestick(x=stock.data.index,
                        open=stock.data['Open'],
                        high=stock.data['High'],
                        low=stock.data['Low'],
                        close=stock.data['Close'], name=stock.name), row=row, col=col)
        col+=1
    row=1
    col=1
    for stock in stocks:
        #Candlestick
        if col == 5:
            col=1
            row+=1
        fig.update_xaxes(title_text=stock.to_string(), row=row,col=col, rangeslider_visible=False)
        fig.update_yaxes(title_text=f"Stock Price (USD per Shares) {stock.purchased_value()}", row=row,col=col)       
        col+=1
    # Add titles
    
    fig.update_layout(title_text="Customizing Subplot Axes", height=1400, font=dict(size=12))
    # X-Axes
    # fig.update_xaxes(
    #     rangeslider_visible=True,
    #     rangeselector=dict(
    #         buttons=list([
    #             dict(count=15, label="15m", step="minute", stepmode="backward"),
    #             dict(count=45, label="45m", step="minute", stepmode="backward"),
    #             dict(count=1, label="HTD", step="hour", stepmode="todate"),
    #             dict(count=3, label="3h", step="hour", stepmode="backward"),
    #             dict(step="all")
    #         ])
    #     )
    # )

    #Show
    fig.show()
stocks = [ model.StockProfile("CLF", 21.50, 223), model.StockProfile("DNN", 1.05, 276.71), 
model.StockProfile("BB", 14.93, 40), model.StockProfile("LEU", 23.75, 10), 
model.StockProfile("LAC", 14.75, 28.06), model.StockProfile("TBPMF", .27, 2750), 
model.StockProfile("DAL", 47.5, 19), model.StockProfile("NCLH", 99.66, 4)]
get(stocks)





