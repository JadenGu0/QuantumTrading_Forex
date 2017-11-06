import pandas as pd


def High(data, period):
    """
    Get the point from Highest Value to the Open Value.
    :param data:
    :param period: The period used for calculate the Highest Value
    :return:
    """
    data = pd.DataFrame(data)
    High_Sub = pd.Series((data.rolling(period).min()['High'] - data['Open']).shift(1), name='High-Sub-' + str(period))
    High_Value = pd.Series(data.rolling(period).min()['High'].shift(1), name='High-Value-' + str(period))
    return High_Sub,High_Value
