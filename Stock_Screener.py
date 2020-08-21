"""A quick prototype of a screener"""
"""Create a reduncacy system or find out whats happening"""
"""MAYBE PAUSING QUERIES FOR A TIME FRAME?"""
import requests
import time
from datetime import datetime
import Filter
import pandas as pd
import time
import troubleshoot
import finance
import getDate
import SpNasdaq
import get_tickers
import company_profile
import collect_data

"""For Stage 2 charts change range to 1 year history"""

present = getDate.getTime()
past = present - 31556926
spclose = SpNasdaq.get_sp500()
companies = get_tickers.get_symbols()

# companies = ['AAPL','FVRR','MSFT','PRPL','WFC']
# companies = companies[:10]
Industry = []
Shares = []
Tickers = []
PriceToday = []
for ticker in companies:
    print(ticker)
    time.sleep(1)
    try:
        r = requests.get('https://finnhub.io/api/v1/stock/candle?symbol={0}&resolution=D&from={1}&to={2}&token=bs79mvnrh5rbhhsbaqkg'.format(ticker,past,present))


        data= r.json()
        # """research"""
        # status,close = Filter.superperformance(data,ticker)
        # if status == True:
        #     industry,shares = company_profile.company_info(ticker)
        #     Industry.append(industry)
        #     Shares.append(shares)
        #     Tickers.append(ticker)
        #     PriceToday.append(close)
        #     collect_data.create_spreadsheet(Tickers,Industry,Shares,PriceToday)
        """stage 2 screener"""
        stage_2 = Filter.checkSMA(data,ticker)
        # time.sleep(1)


        """stage 2 screener"""
        if stage_2:
            finance.plotCandle(data,ticker,spclose)
    except Exception as e:
        print(e)
        """stage 2 screener"""
        time.sleep(3)
        troubleshoot.TryAgain(ticker)
