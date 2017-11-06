import pandas as pd

Period_Front = 10
Period_Back = 10
Distance=150
Point=0.00001
data = pd.read_csv('D:\CSV_Data\EURUSD_1H_FEATURE.csv')
size = len(data.index)
res=[]
for i in range(0, size):
    if i <= Period_Front or i >= (size - Period_Back):
        continue
    else:
        label = 0
        front_df = data.iloc[i - 1 - Period_Front:i - 1]
        back_df = data.iloc[i + 1:i + 1 + Period_Back]
        high_front = front_df.loc[:, ['High']].max().values[0]
        low_front = front_df.loc[:, ['Low']].min().values[0]
        high_back = back_df.loc[:, ['High']].max().values[0]
        low_back = back_df.loc[:, ['Low']].min().values[0]
        openprice=data['Open'][i]
        if high_back >= high_front and low_back >= low_front and (high_front - openprice) >= Point * Distance:
            label=1
        elif low_back <= low_front and high_back <= high_front and (openprice - low_front) >= Point * Distance:
            label=-1
        else:
            label=0
        res.append(label)
res=pd.Series(res,name='Label').shift(Period_Front)
data=data.join(res)

data.to_csv('D:\CSV_Data\EURUSD_1H_FEATURE_LABEL.csv')