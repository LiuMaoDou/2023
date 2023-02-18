import efinance as ef
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import datetime

pd.set_option('mode.chained_assignment', None)

## 指定默认字体
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['font.family'] = 'sans-serif'

## 解决负号’-‘显示为方块的问题
matplotlib.rcParams['axes.unicode_minus'] = False

today = datetime.date.today()
lsday = today - datetime.timedelta(days=14)

end = today.strftime('%Y%m%d')
beg = lsday.strftime('%Y%m%d')


def show_data(id, name, div):
    ft = ef.futures.get_quote_history(quote_ids=id, beg=beg, end=end)
    result = ft[['期货名称', '日期', '收盘']]
    result.is_copy = False
    result.rename(columns={"收盘": name}, inplace=True)
    result.drop(columns=['期货名称'], inplace=True)
    result[name] = round(result[name] / div, 2)
    result.set_index('日期', inplace=True)
    result.plot()


if __name__ == "__main__":
    show_data('114.lhm', '生猪主力', 1000)
    show_data('142.scm', '原油主力', 6.77)
    show_data('115.FGM', '玻璃主力', 1)
    matplotlib.pyplot.show()

# pig_ids = '114.lhm'
# ft = ef.futures.get_quote_history(quote_ids=pig_ids,beg=beg,end=end)
# pig = ft[['期货名称','日期','收盘']]
# pig.rename(columns={"收盘":"生猪主力"}, inplace=True)
# pig.drop(columns=['期货名称'], inplace=True)
# pig['生猪主力'] = round(pig['生猪主力']/1000,2)
# pig.set_index('日期', inplace=True)
# pig.plot()


# pig_ids = '142.scm'
# ft = ef.futures.get_quote_history(quote_ids=pig_ids,beg=beg,end=end)
# oil = ft[['期货名称','日期','收盘']]
# oil.rename(columns={"收盘":"原油主力"}, inplace=True)
# oil.drop(columns=['期货名称'], inplace=True)
# oil['原油主力'] = round(oil['原油主力']/6.77,2)
# oil.set_index('日期', inplace=True)
# oil.plot()
