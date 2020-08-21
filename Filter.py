import matplotlib.dates as mdates
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)

import pandas as pd
from scipy import stats
import DataStructure

def superperformance(data,ticker):
    status = False
    close,high,low,open,date,volume = DataStructure.ConvData(data)
    year_1 = close[-260]
    print('One year ago price was : {0}'.format(year_1))
    supergrowth = (close[-1]/year_1 - 1) * 100
    if supergrowth >= 100 and year_1 >= 20:
        print('You have achieved supergrowth!')
        status = True
        return status,close[-1]
    else:
        return status,close[-1]

def checkSMA(data,ticker):
    close,high,low,open,date,volume = DataStructure.ConvData(data)
    stage_2 = False
    high52 = max(close[-260:])
    low52 = min(close[-260:])
    above = 100*(close[-1] - low52)/(close[-1])
    within = 100*(high52 - close[-1])/close[-1]
    print('52 week high: {0}   52 week low: {1}'.format(high52,low52))
    df = pd.DataFrame(close)

    SMA10 = df.rolling(window=50).mean()
    SMA30 = df.rolling(window=150).mean()
    SMA40 = df.rolling(window=200).mean()

    x = mdates.date2num(date)

    mask =  ~np.isnan(SMA40.values)
    #print(len(x[-len(SMA200[mask]):]))
    #print(len(SMA200[mask]))
    slope, intercept, r_value, p_value, std_err = stats.linregress(x[-len(SMA40[0][-20:]):], SMA40[0][-20:])

    if np.isnan(slope):
        print('Not enough days to calculate slope of SMA40, will give benefit of the doubt.')
        slope = 1
    else:
        print('Slope of SMA200 line : {0}'.format(slope))

    if close[-1] >= 10:
        print('Stock price is greater than 10$')
        if close[-1]> SMA30.values[-1] and close[-1]>SMA40.values[-1]:
            print('Price > SMA150 & SMA200')
            if SMA30.values[-1] > SMA40.values[-1]:
                print('SMA150 > SMA200')
                if SMA10.values[-1] > SMA30.values[-1] and SMA10.values[-1] > SMA40.values[-1]:
                    print('SMA50 > SMA150 & SMA200')
                    if close[-1] > SMA10.values[-1]:
                        print('Price > SMA50')
                        if slope > 0:
                            print('SMA200 is trending up')
                            if above > 30:
                                print('Price is at least 30% above 52 wk low')
                                if within < 25:
                                    print('Price is within 25% of its 52 wk high')
                                    print('**************************')
                                    print('Congrats {0}! You will now be considered to be bought.'.format(ticker))
                                    stage_2 = True

    return stage_2
