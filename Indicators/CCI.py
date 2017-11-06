import pandas as pd


def CCI(data, period, shift):
    """
    Get the CCI value using given data and period
    :param data:
    :param period:
    :param shift:
    :return:
    """
    data = pd.DataFrame(data)
    TP = (data['High'] + data['Low'] + data['Close']) / 3
    CCI = pd.Series((TP - TP.rolling(period).mean()) / (0.015 * TP.rolling(period).std()),
                    name='CCI').shift(1 + shift)
    res_CCI = pd.Series(CCI, name='CCI-' + str(period) + '-' + 'Shift' + str(shift))
    return res_CCI
