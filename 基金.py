import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import tushare as ts
# pro = ts.pro_api('e16391ce58c09028930b9c77f4985f7e4d1c27e1366aded837122c9f')
from ted_funs import *

## 指定默认字体
# matplotlib.rcParams['font.sans-serif'] = ['SimHei']
# matplotlib.rcParams['font.family'] = 'sans-serif'

## 解决负号’-‘显示为方块的问题
# matplotlib.rcParams['axes.unicode_minus'] = False

# 全局,给函数里面result调用
# gp_all = data = pro.query('stock_basic', exchange='', list_status='L', fields='ts_code,name')
# result = gp_all['ts_code'].str.split('.',expand=True)
# result['gp'] = result[1] + result[0]


if __name__ == "__main__":
    single_jj_add('015282')
    # group_add_gp('ETF')
    # add_gp_to_group('SZ000725','ETF')
    # add_gp('SZ000725')
    # df = get_r_gp(gp())
    # group_add_gp(df, '银行')
    # print(df)
    # group_add_gp('ETF')
    # add_gp_group('重点关注')
    # group_add_gp('test', '重点关注')
    # etf = ak.fund_etf_category_sina(symbol="ETF基金")
    # etf = etf['代码'].str.upper()
    # for code in etf:
    #     print(code)
    #     add_gp_to_group(code, 'ETF')