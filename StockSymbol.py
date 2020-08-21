import requests
r = requests.get('https://finnhub.io/api/v1/stock/symbol?exchange=US&token=bs79mvnrh5rbhhsbaqkg')
data=r.json()

print(type(data))

for each in data:
    print(each)
