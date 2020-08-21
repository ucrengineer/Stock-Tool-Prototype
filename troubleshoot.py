import requests
import Filter

def TryAgain(ticker):
    try:
        r = requests.get('https://finnhub.io/api/v1/stock/candle?symbol={0}&resolution=W&from=1485368075&to=1595661232&token=bs79mvnrh5rbhhsbaqkg'.format(ticker))
        print(r)
        data= r.json()
        print(data.keys())
        stage_2 = Filter.checkSMA(data,ticker)
        if stage_2:
            finance.plotCandle(data,ticker)
    except Exception as e:
        print(e)
        print('Trouleshoot failed..')
