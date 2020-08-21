import requests
r = requests.get('https://finnhub.io/api/v1/stock/peers?symbol=AAPL&token=bs79mvnrh5rbhhsbaqkg')
print(r.json())
