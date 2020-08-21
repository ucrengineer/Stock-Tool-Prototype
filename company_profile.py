import requests

def company_info(ticker):
    try:
        r = requests.get('https://finnhub.io/api/v1/stock/profile2?symbol={0}&token=bs79mvnrh5rbhhsbaqkg'.format(ticker))
        data = r.json()
        industry = data['finnhubIndustry']
        shares = data['shareOutstanding']
    except Exception as e:
        print(e)
        industry = 'null'
        shares = 'null'
    return industry, shares
