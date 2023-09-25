import tkinter as tk
from tkinter import filedialog
import re
import pandas as pd
import datetime
import requests
from lxml import etree
import json
import akshare as ak
import os
import efinance as ef


# 全局 #########
os.chdir(os.path.dirname(os.path.abspath(__file__)))
today = datetime.date.today().strftime('%Y%m%d')
cookie = "device_id=57caf4a91ce6ff9c55bbc46a921c7cf9; s=am17pqdsp5; remember=1; xq_is_login=1; u=1231461751; xq_a_token=e25bed64a8c350ae11e5e01099815d79e85cf963; xqat=e25bed64a8c350ae11e5e01099815d79e85cf963; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOjEyMzE0NjE3NTEsImlzcyI6InVjIiwiZXhwIjoxNjkwNTAwODM3LCJjdG0iOjE2ODc5MDg4MzcxNzksImNpZCI6ImQ5ZDBuNEFadXAifQ.rBKZZaHZ6h17nLgh1SXm9PIyQgk9mtXMB6SUjQ24azji3hgq04d6ThiRHG_f3KrTfX5u-MTj8ViyES2e_MJI9lfXaV22XaeH2S8gubsM6msl6GJc_K7OeYHHxWEDZh6k_NfkWtnk6iZNqdgf4nyM3zW8wtZxiUEBPCMsSdeowf2znjtkV3fi04G0QLiKf_u1LNAur4Ul-Cw6Lf2ZMhQBuocMJo_MgysclhfGq-UpwpkRw-UOKxu2wWpyc_Yb9p7PPFbwX0xX9yvHqEhMxysjCbdn69OMzvUBm9wwOC9PVBs-Lpxxk0A0dkJKXIVvSVZt2MXkEdLNv4pvQ57FZikK7g; xq_r_token=68719034ad81954a123c92e964d509be6b6da853; Hm_lvt_1db88642e346389874251b5a1eded6e3=1686437002,1687643648,1687908843; acw_tc=0bdd303616879088481262485ee13006dc0d206c491bcf070f1124a7fe5276; is_overseas=0; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1687908968"
headers = {'cookie': cookie, "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}

# stock_zh_a_spot_em_df = ak.stock_zh_a_spot()
# stock_zh_a_spot_em_df.to_excel('all_gp.xlsx')
result = pd.read_excel("all_gp.xlsx")
# 全局 #########



def input_file_path():
    window = tk.Tk()
    window.title('(^_^))')
    window.geometry('220x20')
    tk.Label(window, text='"Pls Select The File"').pack()
    inpath = filedialog.askopenfilename()
    window.destroy()
    return inpath


def input_folder_path():
    window = tk.Tk()
    window.title('(^_^))')
    window.geometry('220x20')
    tk.Label(window, text='"Pls Select The File"').pack()
    inpath = filedialog.askdirectory()
    window.destroy()
    return inpath

def eastmoney(url, data=None):
    if data is None:
        data = {}
    result = requests.get(url, params=data)
    pattern = re.compile(r'.*?\((.*)\).*', flags=re.S)
    newR = pattern.sub("\g<1>", result.text)
    newR = json.loads(newR)
    return newR

def list_gp():
    url = 'https://stock.xueqiu.com/v5/stock/hot_stock/list.json'
    param = {
        'size': 8,
        '_type': 10,
        'type': 10
    }

    page_text = requests.get(url=url, headers=headers, params=param).text
    print(page_text)


def add_gp(gp):
    url = 'https://stock.xueqiu.com/v5/stock/portfolio/stock/add.json'
    data = {
        'symbols': gp,
        'category': 1
    }
    response = requests.post(url=url, data=data, headers=headers)
    response = json.loads(response.text)
    if response['error_code'] == 0:
        print('股票添加成功')
    else:
        print('股票添加失败,请检查')


def add_gp_group(name):
    url = 'https://stock.xueqiu.com/v5/stock/portfolio/create.json'
    data = {
        'category': 1,
        'pnames': name
    }
    response = requests.post(url=url, data=data, headers=headers)
    response = json.loads(response.text)
    if response['error_code'] == 0:
        print('组添加成功')
    else:
        print('组添加失败,请检查')


def add_gp_to_group(gp, name):
    url = 'https://stock.xueqiu.com/v5/stock/portfolio/stock/modify_portfolio.json'
    data = {
        'symbols': gp,
        'pnames': name,  # 如果多个组,可以写成 'xx1, xx2'
        'category': 1
    }

    response = requests.post(url=url, data=data, headers=headers)
    response = json.loads(response.text)
    if response['error_code'] == 0:
        print('股票添加组成功')
    else:
        print('股票添加组失败,请检查')


def gp():
    df = pro.query('stock_basic', exchange='', list_status='L')
    df.dropna(inplace=True)
    result = df[df['industry'].str.contains('银行')]['industry'].unique()
    df = df[df.industry.isin(result)]
    return df


def get_r_gp(gp_list):
    result = gp_list['ts_code'].str.split('.', expand=True)
    result['股票代码'] = result[1] + result[0]
    return result


def read_jj(path):
    jj_list = pd.read_csv(path)
    # jj = pd.read_excel(path)
    return jj_list


def keep_chinese_english_digits(text):
    pattern = re.compile(r'[^\w\u4e00-\u9fa5]')  # 匹配非中文、非英文和非数字字符的正则表达式
    clean_text = re.sub(pattern, '', text)  # 去除非中文、非英文和非数字字符
    return clean_text

def jijin(id):
    df = ef.fund.get_fund_codes()
    jj_name = df[df['基金代码'].isin([id])].values[0][1]
    jj_name = keep_chinese_english_digits(jj_name)
    # public_dates = ef.fund.get_public_dates(id)
    # dates = public_dates[:1]
    # amount = ef.fund.get_types_percentage(id, dates)
    gp_list = ef.fund.get_invest_position(id)
    return gp_list, jj_name[-8:]  # 雪球只能配置小于8个字符(中文)


def jj_list_add():
    jj_path = '/Users/liujiannan/Desktop/个人基金.csv'
    jj_list = read_jj(jj_path)
    for jj in jj_list['基金代码']:
        # jj_name = jj_list[jj_list['基金代码'].isin([jj])].values[0][0]
        jj = str(jj)
        if len(jj) != 6:
            jj = '0' * (6 - len(jj)) + jj
        gp_list, jj_name = jijin(jj)

        for _ in gp_list['股票代码']:
            xqgp = result[result[0].isin([_])]['gp'].values[0]
            add_gp(xqgp)
            add_gp_group(jj_name)
            add_gp_to_group(xqgp, jj_name)
            print(str(jj_name) + " " + str(xqgp))
    print("Done")


def single_jj_add(single_jj_id):
    gp_list, jj_name = jijin(single_jj_id)
    for code in gp_list['股票代码']:
        xqgp = result[result['代码'].str.contains(code)]['代码'].tolist()[0].upper()
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
