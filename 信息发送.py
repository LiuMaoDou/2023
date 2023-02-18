import pandas as pd
import os
from tkinter import messagebox
from multiprocessing.dummy import Pool
import tushare as ts
import requests
import re
import json
import datetime

key = '8b334e2d5d482292aa8b516c7f59dd6d23c0266dac3dc407dfb63ea1'
pro = ts.pro_api(key)

os.chdir('/Users/liujiannan/Desktop/')
token = 'JQGLmL90YuE4r0BCfpYK2L1M6'

headers = {
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/95.0.4638.69 Safari/537.36"}

today = datetime.date.today().strftime('%Y-%m-%d')


def eastmoney(url, data=None):
    if data is None:
        data = {}
    result = requests.get(url, params=data)
    pattern = re.compile(r'.*?\((.*)\).*', flags=re.S)
    newR = pattern.sub("\g<1>", result.text)
    newR2 = json.loads(newR)
    return newR2


def futures():
    # 生猪 ###################
    url = 'http://futsseapi.eastmoney.com/static/114_lh2209_mx/11?callbackName=jQuery35106817432867056272_1658586689857'
    result = eastmoney(url)
    pig = result['mx'][0]['p']
    content = today + " : " + "生猪2209" + " --> " + str(pig)
    send_message(content)

    # 黄金 ##################
    url = "http://futsseapi.eastmoney.com/list/variety/101/1"
    data = {
        'callbackName': 'jQuery35109938443184047594_1658587384610',
        'orderBy': 'zdf',
        'sort': 'desc',
        'pageSize': '12',
        'pageIndex': '0'
    }
    result = eastmoney(url, data)
    gold = result['list'][0]['p']
    content = today + " : " + "COMEX黄金" + " --> " + str(gold)
    send_message(content)




def bitcoin():
    url = 'https://quotes.sina.cn/fx/api/openapi.php/BtcService.getMinKline?symbol=btcbtcusd&scale=1&datalen=1440' \
          '&callback=var%20_btcbtcusd_1_1655561443342= '

    result = eastmoney(url)
    content = "比特币价格" + " : " + result['result']['data'][-1]['d'] + " --> " + result['result']['data'][-1]['c'] + ' USD'
    send_message(content)


def wti_oil():
    url = 'https://stock2.finance.sina.com.cn/futures/api/openapi.php/GlobalFuturesService.getGlobalFuturesMinLine' \
          '?symbol=CL&callback=var%20t1hf_CL= '
    result = eastmoney(url)
    content = "wti_oil" + " : " + result['result']['data']['minLine_1d'][-1][-1] \
              + " --> " + result['result']['data']['minLine_1d'][-1][1] + " USD"
    send_message(content)


def daily_message(code):
    url = "https://np-anotice-stock.eastmoney.com/api/security/ann"

    data = {
        'cb': 'jQuery1123022120892412089788_1658501631040',
        'sr': '-1',
        'page_size': '50',
        'page_index': '1',
        'ann_type': 'A',
        'client_source': 'web',
        'stock_list': code,
        'f_node': '0',
        's_node': '0',
    }

    result = eastmoney(url, data)

    content = ""

    for item in result['data']['list']:
        if today in item['display_time']:
            http = 'https://data.eastmoney.com/notices/detail/{}/{}.html'.format(code, item['art_code'])
            content += today + " --> " + item['title'] + '\n' + http + '\n'

    if content:
        send_message(content)


def daily_message_snowball(code):
    session = requests.Session()
    main_url = 'https://xueqiu.com/'
    session.get(url=main_url, headers=headers)

    url = 'https://xueqiu.com/statuses/stock_timeline.json'

    data_news = {
        'symbol_id': code,
        'count': '20',
        'source': "自选股新闻",
        'page': '1',
    }

    data_gg = {
        'symbol_id': code,
        'count': '20',
        'source': "公告",
        'page': '1',
    }

    result_news = json.loads(session.get(url, params=data_news, headers=headers).text)
    result_gg = json.loads(session.get(url, params=data_gg, headers=headers).text)

    pattern = re.compile('(.*?) <a href="(.*?)".*')

    content = ""

    for item in result_news['list']:
        time = item['created_at'] / 1000
        time_h = datetime.datetime.fromtimestamp(time).strftime('%Y-%m-%d')
        if time_h == today:
            desc = item['description']

            desc_title = pattern.search(desc).group(1)
            desc_html = pattern.search(desc).group(2)

            content += today + " --> " + item['user']["screen_name"] + " : " + desc_title + '\n' + desc_html + '\n'

    for item in result_gg['list']:
        time = item['created_at'] / 1000
        time_h = datetime.datetime.fromtimestamp(time).strftime('%Y-%m-%d')
        if time_h == today:
            desc = item['description']

            desc_title = pattern.search(desc).group(1)
            desc_html = pattern.search(desc).group(2)

            content += today + " --> " + item['user']["screen_name"] + " : " + desc_title + '\n' + desc_html + '\n'

    if content:
        send_message(content)


def send_message(content):
    flomo_data = {
        'content': "{}".format(content)
    }

    wx_data = {
        'text': '关注',
        '{desp}'.format(desp=flomo_data['content']): "提醒"
    }

    requests.post('https://flomoapp.com/iwh/MjMyNTE1/b2a4807c1ab2855b7f65c745afb248ef/', data=flomo_data)
    requests.post('http://wx.xtuis.cn/{token}.send'.format(token=token), data=wx_data)


def sample():
    data = pro.query('stock_basic', exchange='', list_status='L', fields='ts_code,symbol,name,industry')
    send_message(data.sample(n=1))

if __name__ == '__main__':

    bitcoin()
    # wti_oil()
    # futures()
    #
    # df = pd.read_csv('message_source.csv')
    #
    # df.set_index('code', inplace=True)
    # codeLists = df.index.to_list()
    #
    # pool = Pool(10)
    # # pool.map(daily_message, codeLists)
    # pool.map(daily_message_snowball, codeLists)
    #
    # pool.close()
    # pool.join()
    sample()





    messagebox.showinfo('股票', '...完成任务...')
    print("---Finished---")
