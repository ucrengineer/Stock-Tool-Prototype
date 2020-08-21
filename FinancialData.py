import requests
import pandas as pd
import finnhub



def find_earnings(data_file,frequency):
    for each in data_file:
        # qt.append(each['quarter'])
        ic.append(each['report']['ic'])
    # ic = f[2]['report']['ic']
    # df = pd.DataFrame({'earnings':ic,'quarter':qt})
    # print(df.head())

    earnings = []
    i = 0
    for each in ic:

        for each in each:

            if each['concept'] == 'EarningsPerShareDiluted':
                earnings.append(each['value'])
                qt.append(data_file[i]['{0}'.format(frequency)])

                i+=1
    df = pd.DataFrame({'earnings':earnings,'{0}'.format(frequency):qt})
    print(df.head())
    # recent quarters are first
    quarter_1 = []
    quarter_2 = []
    quarter_3 = [0]
    if frequency == 'quarter':
        i = 0
        for each in df['{0}'.format(frequency)]:

            if each == 1:
                # print('index earnings')
                print(df.loc[[i]])
                quarter_1.append(df['earnings'][i])

            if each == 2:
                # print('index earnings')
                print(df.loc[[i]])
                quarter_2.append(df['earnings'][i])

            if each == 3:
                # print('index earnings')
                print(df.loc[[i]])
                quarter_3.append(df['earnings'][i])
            i +=1
    print(quarter_1)
    print(quarter_2)
    print(quarter_3)



r = requests.get('https://finnhub.io/api/v1/stock/financials-reported?cik=320193&freq=annual&symbol=GRVY&token=bs79mvnrh5rbhhsbaqkg')
annual_data = r.json()
g = annual_data['data']

r = requests.get('https://finnhub.io/api/v1/stock/financials-reported?cik=320193&freq=quarterly&symbol=GRVY&token=bs79mvnrh5rbhhsbaqkg')
data = r.json()
#print(data.keys())
f = data['data']
ic = []
qt = []

# year or quarter
find_earnings(f,'quarter')
