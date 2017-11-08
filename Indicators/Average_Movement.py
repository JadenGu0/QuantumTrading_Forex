import pandas as pd


def Average_Movement(data, period, shift, point):
    """
    Calculate the average movement using the given period and data
    :param data:
    :param period:
    :param shift:
    :param point:
    :return:
    """
    data = pd.DataFrame(data)
    move = (data['Close'] - data['Open']) / point
    AM = pd.Series(move.rolling(period).mean().shift(shift),
                   name='Average_Movement-' + str(period) + '-Shift-' + str(shift))
    data=data.join(AM)
    return data
