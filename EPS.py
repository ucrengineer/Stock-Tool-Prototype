import requests
r = requests.get('https://finnhub.io/api/v1/calendar/earnings?from=2019-06-12&to=2020-06-15&token=bs79mvnrh5rbhhsbaqkg')

data = r.json()

print(data.keys())
