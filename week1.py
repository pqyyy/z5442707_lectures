import yfinance
tic = "QAN.AX"
start = '2020-01-01'
end = None
df = yfinance.download(tic, start, end, ignore_tz=True)
print(df)
df.to_csv('qan_stk_prc.csv')


"""
dict = {}
    for ticker in tickers_lst:
        exchange = tic_exchange_dic[ticker]

        data = []
        for line in read_dat(ticker):
            record = {}
            for col in col_lst:
                record[col] = line_to_dict(line)[col]
            data.append(record)

        dict[ticker] = {'exchange':exchange, 'data':data}

        return dict






dict = {}
for tic in tickers_lst:
    tic_dict = {}
    tic_dict['exchange'] = tic_exchange_dic[tic]


    data = []
    for line in read_dat(ticker):
        for col in col_lst:
            data = [{col: line_to_dict(line)[col]}]

    tic_dict['data'] = data

    dict[tic] = tic_dict
"""
