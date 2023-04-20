import efinance as ef
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import tushare as ts
pro = ts.pro_api('e16391ce58c09028930b9c77f4985f7e4d1c27e1366aded837122c9f')
from 雪球 import *

## 指定默认字体
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['font.family'] = 'sans-serif'

## 解决负号’-‘显示为方块的问题
matplotlib.rcParams['axes.unicode_minus'] = False

# 全局,给函数里面result调用
gp_all = data = pro.query('stock_basic', exchange='', list_status='L', fields='ts_code,name')
result = gp_all['ts_code'].str.split('.',expand=True)
result['gp'] = result[1] + result[0]

def gp():
    df = pro.query('stock_basic', exchange='', list_status='L')
    df.dropna(inplace=True)
    result = df[df['industry'].str.contains('银行')]['industry'].unique()
    df = df[df.industry.isin(result)]
    return df


def get_r_gp(gp_list):
    result = gp_list['ts_code'].str.split('.',expand=True)
    result['股票代码'] = result[1] + result[0]
    return result



def read_jj(path):
    jj_list = pd.read_csv(path)  
    # jj = pd.read_excel(path)
    return jj_list

def jijin(id):
    df = ef.fund.get_fund_codes()
    jj_name = df[df['基金代码'].isin([id])].values[0][1]
    # public_dates = ef.fund.get_public_dates(id)
    # dates = public_dates[:1]
    # amount = ef.fund.get_types_percentage(id, dates)
    gp_list = ef.fund.get_invest_position(id)
    return gp_list, jj_name[-8:] # 雪球只能配置小于8个字符(中文)


def jj_list_add():
    jj_path = '/Users/liujiannan/Desktop/个人基金.csv'
    jj_list = read_jj(jj_path)
    for jj in jj_list['基金代码']:
        # jj_name = jj_list[jj_list['基金代码'].isin([jj])].values[0][0]
        jj = str(jj)
        if len(jj) != 6:
            jj = '0'*(6-len(jj)) + jj
        gp_list, jj_name = jijin(jj)

        for _ in gp_list['股票代码']:
            xqgp = result[result[0].isin([_])]['gp'].values[0]
            add_gp(xqgp)
            add_gp_group(jj_name)
            add_gp_to_group(xqgp,jj_name)
            print(str(jj_name) + " " + str(xqgp))   
    print("Done")


def single_jj_add(single_jj_id):
    gp_list, jj_name = jijin(single_jj_id)
    # jj_name = jj_name[:8]
    for _ in gp_list['股票代码']:
        xqgp = result[result[0].isin([_])]['gp'].values[0]
        add_gp(xqgp)
        add_gp_group(jj_name)
        add_gp_to_group(xqgp,jj_name)
        print(str(jj_name) + " " + str(xqgp)) 
    print("Done")


def group_add_gp(gp_list, group_name):
    path = '/Users/liujiannan/Desktop/股票输入.csv'
    # path = '/Users/liujiannan/etf.csv'
    gp_list = pd.read_csv(path)
    for i in gp_list['股票代码']:
        print(i)
        add_gp_to_group(i, group_name)
        
    print("Done")


if __name__ == "__main__":
    # single_jj_add('011966')
    # group_add_gp('ETF')
    # add_gp_to_group('SZ000725','ETF')
    # add_gp('SZ000725')
    # df = get_r_gp(gp())
    # group_add_gp(df, '银行')
    # print(df)
    # group_add_gp('ETF')
    # add_gp_group('重点关注')
    group_add_gp('test', '重点关注')