import matplotlib.pyplot as plt
from mpl_finance import candlestick_ohlc
import pandas as pd
import matplotlib.dates as mpl_dates
import requests
from datetime import datetime
import numpy as np
import matplotlib

def ConvData(data):
    close = data['c']
    high = data['h']
    low = data['l']
    open = data['o']
    dates = data['t']
    volume = data['v']
    date = []
    for each in dates:
        Ddate = datetime.fromtimestamp(each).strftime("%Y-%m-%d")
        date.append(np.datetime64(Ddate))

    date = np.array(date)

    return close,high,low,open,date,volume
