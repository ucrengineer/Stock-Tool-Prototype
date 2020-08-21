import requests
r = requests.get('https://finnhub.io/api/v1/stock/symbol?exchange=US&token=bs79mvnrh5rbhhsbaqkg')
data = r.json()
symbols = []
def get_symbols():
    for each in data:
        symbols.append(each['symbol'])

    return symbols
