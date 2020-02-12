#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 20:23:41 2020

@author: marissa
"""

#this script will plot 2 technical indicators Simple Moving Average and Relative Strength Index, in realtime
#it also saves in your local an excel file with hourly price of the stock
#mute any functions with the hashtag in front of the line of code


#replace my API key with your own API key from https://www.alphavantage.co/. The Alpha Vantage API Key is able to do 
#5 calls within a minute which is not bad, and up to 500 calls a day for the free version

import pandas as pd
apikey = '4NU24I6VRCGT040D'
from alpha_vantage.timeseries import TimeSeries
import time
import matplotlib.pyplot as plt
from alpha_vantage.techindicators import TechIndicators

#change your ticker to the stock you follow. Instead of 'AMZN' change it to 'PTPP'
stock = TimeSeries(key=apikey,output_format ='pandas')
data, metadata = stock.get_intraday(symbol = 'AMZN', interval ='60min', outputsize ='full')
print (data)

i = 1
while 1 ==1:
    data, metadata = stock.get_intraday(symbol = 'AMZN', interval ='60min', outputsize ='full')
    data.to_excel("AMZN.xlsx")
    time.sleep(60)

#Tech Indicators - Relative Strength Indicator (RSI) High RSI overbought, Low RSI oversold
period = 60
techind = TechIndicators(key = apikey, output_format = 'pandas')
datatechind, metadata_techind = techind.get_rsi(symbol = 'AMZN', interval = '60min',
                                           time_period = period, series_type= 'close')

datasma, metadatasma = techind.get_sma(symbol ='AMZN',interval = '60min',
                                           time_period = period, series_type= 'close')

df1 = datasma.iloc[1::]
df2 = datatechind
df1.index = df2.index

fig, axis1 = plt.subplots()
axis1.plot(df1)
axis2 = axis1.twinx()
axis2.plot(df2, 'r.')
plt.title('RSI and SMA Graph',)
plt.show()

