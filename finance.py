import pandas as pd
from datetime import datetime
import requests
import mplfinance as mpf
import DataStructure
import SpNasdaq
from operator import truediv
import matplotlib.pyplot as plt



def plotCandle(data,ticker,spclose):
    fileloc = '/home/ucrengineer/Stock Application/'

    close,high,low,open,dates,volume = DataStructure.ConvData(data)
    ohlc = pd.DataFrame({'Date':dates,'Open':open,'High':high,'Low':low,'Close':close,'Volume':volume})
    ohlc.set_index('Date',inplace=True, drop=True)
    res500 = list(map(truediv, close, spclose))
    # resDAQ = list(map(truediv, close, nclose))
    RS = pd.DataFrame({'SP': res500})

    kwargs = dict(type='candle',mav=(50,150,200),volume=True,figratio=(18,10),figscale=2)
    mc = mpf.make_marketcolors(up='k',down='r',inherit=True)
    s  = mpf.make_mpf_style(base_mpf_style='classic',marketcolors=mc)
    apdict = mpf.make_addplot(RS,mav = 30,panel=2,type='line',ylabel='RS')
    try:
        mpf.plot(ohlc,**kwargs,addplot=apdict,panel_ratios=(3,1),style=s,title='{0}'.format(ticker),savefig='{0}ChartBook/{1}.png'.format(fileloc,ticker))
    except Exception as e:
        mpf.plot(ohlc,**kwargs,style=s,title='{0}'.format(ticker),savefig='{0}ChartBook/{1}.png'.format(fileloc,ticker))

    plt.close('all')
