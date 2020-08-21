import requests
r = requests.get('https://finnhub.io/api/v1/stock/metric?symbol=AAPL&metric=all&token=bs79mvnrh5rbhhsbaqkg')
print(r.json())
