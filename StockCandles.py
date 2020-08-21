import requests
import matplotlib.pyplot as plt
import time
from datetime import datetime
import PlotTicker
import numpy as np

r = requests.get('https://finnhub.io/api/v1/stock/candle?symbol=IMAX&resolution=D&from=1531900375&to=1595058775&token=bs79mvnrh5rbhhsbaqkg')

data= r.json()


dates = data['t']
close = np.array(data['c'])
volume = np.array(data['v'])
date = []
for each in dates:
    Ddate = datetime.fromtimestamp(each).strftime("%Y-%m-%d")
    date.append(np.datetime64(Ddate))

date = np.array(date)
SMA50,SMA150,SMA200,stage_2 = PlotTicker.checkSMA(date,close)
print(stage_2)
PlotTicker.plot('AAPL',date,close,SMA50,SMA150,SMA200)
