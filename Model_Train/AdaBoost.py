import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import train_test_split
from sklearn.metrics import classification_report
from sklearn.preprocessing import Imputer
from sklearn.ensemble import AdaBoostClassifier
data_train = pd.read_csv('D:\CSV_Data\EURUSD_1H_FEATURE_LABEL_TRAIN.csv')
data_test = pd.read_csv('D:\CSV_Data\EURUSD_1H_FEATURE_LABEL_TEST.csv')
all_feature=list(data_train.columns)
all_feature.remove('Label')
all_feature.remove('Close')
all_feature.remove('Time (UTC)')
all_feature.remove('Volume ')
all_feature.remove('Unnamed: 0')
x_train = data_train.loc[:, all_feature]
x_test = data_test.loc[:, all_feature]
x_train=Imputer().fit_transform(x_train)
x_test=Imputer().fit_transform(x_test)
y_train = data_train.loc[:, ['Label']]
y_test = data_test.loc[:, ['Label']]
rf=AdaBoostClassifier().fit(x_train, y_train)
print rf
print('Training done')
answer_dt = rf.predict(x_test)
print('Prediction done')
print('\n\nThe classification report for RF:')
print(classification_report(y_test, answer_dt))