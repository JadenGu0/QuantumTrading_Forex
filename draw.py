import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv('D:\CSV_Data\EURUSD_1H_FEATURE_LABEL.csv', nrows=1000)
fig = plt.figure()
ax1=fig.add_subplot(3,1,1)
ax2=fig.add_subplot(3,1,2)
ax1.plot(data['Close'],'g-',label='Close Price')
ax2.plot(data['Label'])
fig.legend()
plt.show()
