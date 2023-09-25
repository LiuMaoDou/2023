import efinance as ef
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import tushare as ts
import os
from datetime import datetime, timedelta
## 指定默认字体
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['font.family'] = 'sans-serif'

## 解决负号’-‘显示为方块的问题
matplotlib.rcParams['axes.unicode_minus'] = False


today = datetime.now().date()

dayn = datetime.now().date()
day1 = today - timedelta(days=7)

dayn = dayn.strftime('%Y%m%d')
day1 = day1.strftime('%Y%m%d')

pro = ts.pro_api('e16391ce58c09028930b9c77f4985f7e4d1c27e1366aded837122c9f')

os.chdir('/Users/liujiannan/Desktop/股票')
file = '股票.xlsx'

result = pd.read_excel(file)
lst = result['股票代码']

for gp in lst:
    # 获取列2中，列1等于3的对应值
    name = result.loc[result['股票代码'] == gp, '股票名']
    value = name[name.index.tolist()[0]]

    df = pro.daily(ts_code=gp, start_date=day1, end_date=dayn)  
    print(df)
    # df['trade_date'] = pd.to_datetime(df['trade_date'])
    df = df.sort_values('trade_date')
    plt.plot(df['trade_date'], df['close'])
    plt.xlabel('日期')
    plt.ylabel('收盘价')
    plt.title(value)
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()
