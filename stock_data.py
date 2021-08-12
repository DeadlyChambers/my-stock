from pandas_datareader import data as pdr
from datetime import date, datetime, timedelta
import yfinance as yf
yf.pdr_override()
import pandas as pd

ticker_list = ['CLF', 'DNN', 'TBPMF','LEU', 'DAL', 'BB', 'LAC', 'NCLH']
today = date.today()
# We can get data by our choice by giving days bracket
end_date = today
start_date = today + timedelta(-2)


files=[]
def getData(ticker):
    print (ticker)
    data = pdr.get_data_yahoo(ticker, start=start_date, end=end_date)
    dataname= ticker+'_'+str(today)
    files.append(dataname)
    SaveData(data, dataname)

# Create a data folder in your current dir.
def SaveData(df, filename):
    df.to_csv('~/usr/data/'+filename+'.csv')

#This loop will iterate over ticker list, will pass one ticker to get data, and save that data as file.
def update():
    for tik in ticker_list:
        getData(tik)

    for i in range(0,len(ticker_list)):
        df1= pd.read_csv('~/usr/data/'+ str(files[i])+'.csv')
    print (df1.head())