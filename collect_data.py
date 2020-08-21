import pandas as pd


def create_spreadsheet(tickers,industrys,shares,close):

    df = pd.DataFrame({'ticker':tickers,'Industry':industrys,
                        'shares':shares,'price':close})



    # Create a Pandas Excel writer using XlsxWriter as the engine.
    writer = pd.ExcelWriter('stock_and_shares.xlsx')

    # Convert the dataframe to an XlsxWriter Excel object.
    df.to_excel(writer, sheet_name='Sheet1', index=False)

    # Close the Pandas Excel writer and output the Excel file.
    writer.save()
