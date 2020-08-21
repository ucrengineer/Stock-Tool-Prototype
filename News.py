import requests
r = requests.get('https://finnhub.io/api/v1/news?category=general&token=bs79mvnrh5rbhhsbaqkg')
print(r.json())
