import pandas as pd


def Low(data, period):
    """
    et the point from Lowest Value to the Open Value.
    :param data:
    :param period:
    :return:
    """
    data = pd.DataFrame(data)
    Low_Sub = pd.Series((data['Open'] - data.rolling(period).min()['Low'].shift(1)), name='Low-Sub-' + str(period))
    Low_Value = pd.Series( data.rolling(period).min()['Low'].shift(1), name='Low-Value-' + str(period))
    data=data.join(Low_Sub)
    data=data.join(Low_Value)
    return data
