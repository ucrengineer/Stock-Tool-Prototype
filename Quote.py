import requests
r = requests.get('https://finnhub.io/api/v1/quote?symbol=AAPL&token=bs79mvnrh5rbhhsbaqkg')
print(r.json())
# use websocket for live updating
