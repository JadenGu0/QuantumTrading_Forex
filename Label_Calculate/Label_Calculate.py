import pandas as pd


def Label_Calculate(data=None, period=10, point=0.00001, profit=200, stoploss=200):
    """

    :param data:
    :param period:
    :param point:
    :param profit:
    :param stoploss:
    :return:
    """
    size = len(data.index)
    res = []
    for i in range(0, size):
        label = 0
        if i >= (size - period):
            res.append(label)
            continue
        else:
            back_df = data.iloc[i + 1:i + 1 + period]
            high_back = back_df.loc[:, ['High']].max().values[0]
            low_back = back_df.loc[:, ['Low']].min().values[0]
            openprice = data['Open'][i]
            if (high_back - openprice) >= profit * point and (openprice - low_back) < stoploss * point:
                label = 1
            if (openprice - low_back) >= profit * point and (high_back - openprice) <= stoploss * point:
                label = -1
            res.append(label)
    res = pd.Series(res, name='Label')
    data = data.join(res)
    return data
