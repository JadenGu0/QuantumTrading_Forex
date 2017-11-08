import pandas as pd


def MA(data, period, shift):
    """
    Get the MA value using given data and period
    :param data:
    :param period:
    :param shift:
    :return:
    """
    data = pd.DataFrame(data)
    MA = pd.Series(data.rolling(period).mean()['Close'].shift(1 + shift),
                   name='MA-' + str(period) + '-Shift-' + str(shift))
    data=data.join(MA)
    return data
