import requests
r = requests.get('https://finnhub.io/api/v1/company-news?symbol=AAPL&from=2020-04-30&to=2020-05-01&token=bs79mvnrh5rbhhsbaqkg')
print(r.json())
