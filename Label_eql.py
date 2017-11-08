import pandas as pd
from Label_Calculate.Label_Calculate import Label_Calculate

if __name__ == '__main__':
    data = pd.read_csv('D:\CSV_Data\EURUSD_1H_FEATURE.csv')
    data = Label_Calculate(data=data, period=15, point=0.00001, profit=300, stoploss=300)
    data=data.loc[150:,]
    train=data.loc[0:len(data.index)*0.7,data.columns]
    test=data.loc[len(data.index)*0.7+1:len(data.index),data.columns]
    train.to_csv('D:\CSV_Data\EURUSD_1H_FEATURE_LABEL_Train.csv')
    test.to_csv('D:\CSV_Data\EURUSD_1H_FEATURE_LABEL_Test.csv')
    data.to_csv('D:\CSV_Data\EURUSD_1H_FEATURE_LABEL.csv')



