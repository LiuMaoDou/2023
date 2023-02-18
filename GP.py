import tushare as ts
import pandas as pd
import numpy as np
import datetime
import os
import xlwings as xw
import time
from tkinter import messagebox
import sys
# from ef_data import get_data

pd.options.mode.chained_assignment = None

pro = ts.pro_api('8b334e2d5d482292aa8b516c7f59dd6d23c0266dac3dc407dfb63ea1')
os.chdir('/Users/liujiannan/Desktop')

lb_cb = 'jQuery112408386016515502619_1641826224604'  # 量比cb
lb_fields = 'f10,f12,f14'
lb_url = 'https://86.push2.eastmoney.com/api/qt/clist/get'  # 量比url


def timer(function):
    """
    装饰器函数timer
    :param function:想要计时的函数
    :return:
    """

    def wrapper(*args, **kwargs):
        time_start = time.time()
        res = function(*args, **kwargs)
        cost_time = time.time() - time_start
        print("【%s】运行时间：【%s】秒" % (function.__name__, cost_time))
        return res

    return wrapper


# def get_lb():
#     lb_df = get_data(lb_url, lb_cb, lb_fields)
#     df = pd.DataFrame(lb_df)
#     df.columns = ['量比', '代码', 'name']
#     data_tu = pro.stock_basic(exchange='', list_status='L', fields='ts_code')
#     data_tu['代码'] = data_tu['ts_code'].str[:6]
#
#     data = pd.merge(data_tu, df, how='left', on='代码')
#     data.drop(['name', '代码'], axis=1, inplace=True)
#     create_excel_new("股票.xlsx", "股票", '量比', data, "量比")


# 每周更新一次股票列表
def update_gp_list():
    data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,name,industry,market')
    # data.to_excel('股票.xlsx')
    data.replace(np.nan, "无数据", inplace=True)

    df_gp = pd.read_excel('股票.xlsx')
    newdata = df_gp[['ts_code', 'name', 'industry', 'market']]
    df_merge = pd.merge(newdata, data, how='outer', on="ts_code")
    df_merge_n = df_merge.loc[df_merge.isna().any(1)]
    df_merge_n.drop(['name_x', 'industry_x', 'market_x'], axis=1, inplace=True)

    wb = xw.Book('股票.xlsx')
    sheet = wb.sheets['股票']
    num_col = sheet.range('A1').end('right').column
    num_row = sheet.range('A1').end('down').row

    sheet.range(((num_row + 1), 1)).options(index=False, header=False).value = df_merge_n

    num_row_n = sheet.range('A1').end('down').row

    sheet.range((num_row, 1), (num_row, num_col)).copy()
    sheet.range((num_row + 1, 1), (num_row_n, num_col)).paste("formats")
    sheet.range((num_row + 1, 1), (num_row_n, num_col)).autofit()


def ts_date(ttoday=True):
    if ttoday:
        today = datetime.date.today()
    else:
        today = datetime.date.today() - datetime.timedelta(days=1)

    if today.isoweekday() > 5:
        today = today - datetime.timedelta(days=(today.isoweekday() % 5))
        ysday = today - datetime.timedelta(days=1)
        today = today.strftime('%Y%m%d')
        ysday = ysday.strftime('%Y%m%d')
    else:
        ysday = (today - datetime.timedelta(days=1)).strftime('%Y%m%d')
        today = today.strftime('%Y%m%d')

    return today, ysday


def create_excel_new(bookname, sheetname, title, df, df_value):
    print("---Excel Started---")
    wb = xw.Book(bookname)
    sheet = wb.sheets[sheetname]
    num_col = sheet.range('A1').end('right').column
    num_row = sheet.range('A1').end('down').row

    df_gp = pd.read_excel(bookname, sheet_name=sheetname)
    # df_merge = pd.merge(df_gp, df, how='outer', on="ts_code")
    df_merge = pd.merge(df_gp, df, how='left', on="ts_code")

    sheet.range((1, (num_col + 1))).options(index=False).value = df_merge[df_value]
    sheet.range((1, (num_col + 1))).value = title
    sheet.range((1, num_col), (num_row, num_col)).copy()

    sheet.range((1, (num_col + 1)), (num_row, num_col + 1)).paste("formats")
    sheet.range((1, (num_col + 1)), (num_row, num_col + 1)).autofit()

    wb.save(bookname)
    print("---Excel Finished---")


def daily_pct_new(date):
    daily = pro.daily(trade_date=date, fields="ts_code,pct_chg,close,amount")
    create_excel_new("股票.xlsx", "股票", date, daily, 'pct_chg')
    create_excel_new("股票.xlsx", "股票", '股价', daily, 'close')


def reven(year, Q):
    q = {"Q1": str(year) + "0331", "Q2": str(year) + "0630",
         "Q3": str(year) + "0930", "Q4": str(year) + "1231"}
    reven_value = pro.income_vip(period=q[Q], fields='ts_code,ann_date,f_ann_date,end_date,total_revenue,'
                                                     'n_income_attr_p')
    reven_value2 = reven_value.set_index('ts_code')
    reven_value2 = reven_value2[~reven_value2.index.duplicated(keep='last')]
    create_excel_new("股票.xlsx", "股票", str(year) + Q + "-收入", reven_value2, "total_revenue")
    create_excel_new("股票.xlsx", "股票", str(year) + Q + "-利润", reven_value2, "n_income_attr_p")


# def indus_index(today):
#     data = pro.ths_daily(trade_date=today, fields='ts_code,pct_change')
#     create_excel_new("股票.xlsx", "行业", today, data, 'pct_change')
#
#
# def etf(today):
#     etf_data = pro.fund_daily(trade_date=today, fields="ts_code, pct_chg, amount")
#     create_excel_new("股票.xlsx", "ETF", today, etf_data, 'pct_chg')
#     create_excel_new("股票.xlsx", "ETF", today, etf_data, 'amount')


def pe_mv(today):
    # PE和市值
    s_pe = pro.daily_basic(ts_code='', trade_date=today, fields='ts_code,pe_ttm,total_mv')
    s_pe = s_pe.set_index('ts_code')
    create_excel_new("股票.xlsx", "股票", "PE", s_pe, "pe_ttm")
    create_excel_new("股票.xlsx", "股票", "市值", s_pe, "total_mv")
    # PE和市值


@timer
def main():
    today, ysday = ts_date()
    print("Today is", today)
    # print(sys.version)
    #
    # reven(2022, "Q2")



    # daily_pct_new("20220620")
    daily_pct_new(today)
    # indus_index(today)
    # etf(today)
    # update_gp_list()

    # get_lb()
    # print(pro.daily(trade_date=today, fields="ts_code,pct_chg,close,amount"))


if __name__ == "__main__":
    print("---Starting---")
    main()
    messagebox.showinfo('股票', '...完成任务...')
    print("---Finished---")
