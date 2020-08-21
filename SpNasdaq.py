import finance
import getDate
import requests
import time
import DataStructure

index = []
Time = getDate.getTime()
tickers = ['SPY']
def get_sp500():
    for Index in tickers:
        r = requests.get('https://finnhub.io/api/v1/stock/candle?symbol={0}&resolution=D&from=1485368075&to={1}&token=bs79mvnrh5rbhhsbaqkg'.format(Index,Time))

        data= r.json()
        index.append(data)


    sp500 = index[0]
    spclose,sphigh,splow,spopen,spdates,spvolume = DataStructure.ConvData(sp500)
    return spclose
    # nasdaq = index[1]


    # nclose,nhigh,nlow,nopen,ndates,nvolume = DataStructure.ConvData(nasdaq)
