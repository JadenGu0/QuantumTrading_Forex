import pandas as pd


def BB(data, period, shift):
    """
    Get the BBands value using given data and period.
    :param data:
    :param period:
    :return:
    """
    data = pd.DataFrame(data)
    MA = pd.Series(data.rolling(period).mean()['Close'])
    SD = pd.Series(data.rolling(period).std()['Close'])
    b1 = MA + (2 * SD)
    B1 = pd.Series(b1, name='UP BB-' + str(period) + '-' + 'Shift' + str(shift)).shift(1 + shift)

    b2 = MA - (2 * SD)
    B2 = pd.Series(b2, name='DOWN BB-' + str(period) + '-' + 'Shift' + str(shift)).shift(1 + shift)
    return B1, B2
