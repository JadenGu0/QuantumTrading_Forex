import pandas as pd
PERIOD = 4
chunker = pd.read_csv('D:\CSV_Data\EURUSD_15 Mins_Ask_2006.01.01_2017.10.30.CSV', chunksize=PERIOD)
res = pd.DataFrame()
for i in chunker:
    start_time = i[i.columns[0]][0:1].values[0]
    open_price = i[i.columns[1]][0:1].values[0]
    high_price = i[i.columns[2]].max()
    low_price = i[i.columns[3]].min()
    close_price = i[i.columns[4]][-1:].values[0]
    volum = i[i.columns[5]].sum()
    new_data = pd.DataFrame([[start_time, open_price, high_price, low_price, close_price, volum]],
                            columns=i.columns)
    res = pd.concat([res, new_data], ignore_index=True)
res.to_csv('D:\CSV_Data\EURUSD_1H.csv',index=None)
