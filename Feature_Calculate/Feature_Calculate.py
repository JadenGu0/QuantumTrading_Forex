from Indicators.CCI import CCI
from Indicators.Average_Movement import Average_Movement
from Indicators.MA import MA
from Indicators.BB import BB
from Indicators.MAX import High
from Indicators.MIN import Low

def Feature_Calculate(data,point):
    """

    :param data:
    :param point:
    :return:
    """
    data = MA(data, 5, 0)
    data = MA(data, 5, 1)
    data = MA(data, 10, 0)
    data = MA(data, 10, 1)
    data = MA(data, 20, 0)
    data = MA(data, 20, 1)
    data = MA(data, 50, 0)
    data = MA(data, 50, 1)
    data = MA(data, 100, 0)
    data = MA(data, 100, 1)
    data = CCI(data, 5, 0)
    data = CCI(data, 5, 1)
    data = CCI(data, 10, 0)
    data = CCI(data, 10, 1)
    data = CCI(data, 20, 0)
    data = CCI(data, 20, 1)
    data = CCI(data, 50, 0)
    data = CCI(data, 50, 1)
    data = CCI(data, 100, 0)
    data = CCI(data, 100, 1)
    data=High(data,10)
    data=Low(data,10)
    data=High(data,20)
    data=Low(data,20)
    data=High(data,50)
    data=Low(data,50)
    data=High(data,100)
    data=Low(data,100)
    data=BB(data,10,0)
    data=BB(data,20,0)
    data=BB(data,50,0)
    data=BB(data,100,0)
    data = Average_Movement(data, 1, 0, point)
    data = Average_Movement(data, 3, 0, point)
    data = Average_Movement(data, 5, 0, point)
    data = Average_Movement(data, 10, 0, point)
    data = Average_Movement(data, 50, 0, point)
    data = Average_Movement(data, 100, 0, point)
    return data
    # data.to_csv('D:\CSV_Data\EURUSD_1H_FEATURE.CSV', index=None, float_format='%.5f')
