import pandas as pd
import tushare as ts
from sqlalchemy import create_engine, text
import pymysql
import datetime
from datetime import date, timedelta
from ted_funs import eastmoney

pro = ts.pro_api('8b334e2d5d482292aa8b516c7f59dd6d23c0266dac3dc407dfb63ea1')
pymysql.install_as_MySQLdb()
engine_ts = create_engine('mysql://root:Wayne1986@127.0.0.1:3306/股票')

today = datetime.date.today().strftime('%Y%m%d')

# '数据库类型://用户名:口令@机器地址:端口号/数据库名'
# today = datetime.date.today().strftime('%Y%m%d')

def read_data(query):
    df = pd.read_sql_query(con=engine_ts.connect(), sql=text(query))
    return df


def update_gpList():
    df = pro.stock_basic()
    df.to_sql('stock_basic', engine_ts, index=False, if_exists='replace', chunksize=5000)
    print("GP List Update Done...")
    query = "SELECT COUNT(*) FROM stock_basic"
    result = read_data(query)
    print("Total GP No. is " + str(result.iloc[0]['COUNT(*)']))


def gp_daily(days):
    # df = pro.daily(trade_date='20230301')
    # df.to_sql('gp_daily', engine_ts, index=False, if_exists='replace', chunksize=5000)
    for day in days:
        df = pro.daily(trade_date=day)
        df.to_sql('gp_daily', engine_ts, index=False, if_exists='append', chunksize=5000)
        print(day + " finished...")

    print("-----------------------")
    print("Daily_GP Update Done...")
    query = "SELECT trade_date FROM gp_daily"
    result = read_data(query)
    num = len(result['trade_date'].unique())

    print("Total dates No. is " + str(num))


def up_limit(days):
    for day in days:
        df = pro.limit_list_d(trade_date=day, limit_type='U', fields='ts_code,trade_date,industry,name')
        df.to_sql('limit_list_d', engine_ts, index=False, if_exists='append', chunksize=5000)
        print(day + " finished...")

    print("-----------------------")
    print("涨停板数据入库成功...")
    query = "SELECT trade_date FROM limit_list_d"
    result = read_data(query)
    num = len(result['trade_date'].unique())

    print("一共有{}天数据...".format(num))

# def write_data(df):
#     res = df.to_sql('stock_basic', engine_ts, index=False, if_exists='append', chunksize=5000)
#
# def get_data(value):
#     # pro = ts.pro_api()
#     if value == "gpList":
#         df = pro.stock_basic()
#     return df

def count_days(firstday):
    start_date_str = firstday

    # 将输入的字符串转换为日期对象
    start_date = date.fromisoformat(start_date_str)

    # 获取今天的日期
    today = date.today()
    lst = []
    # 打印从某一天到今天的日期
    delta = timedelta(days=1)
    while start_date <= today:
        lst.append(start_date.strftime('%Y%m%d'))
        start_date += delta
    return lst


# def up_limit(day):
#     df01 = pro.stk_limit(trade_date=day, fields="ts_code, up_limit")
#     df02 = pro.daily(trade_date=day, fields="ts_code, close")
#     merged_df = pd.merge(df01, df02, on='ts_code', how='inner')
#     df = merged_df.fillna(0)
#     df['Same'] = df['up_limit'].eq(df['close'])
#     result = df[df['Same']]['ts_code']
#     return result

def daily_money():
    url = "https://push2delay.eastmoney.com/api/qt/clist/get"
    data = {
        "cb": "jQuery112309315694094136504_1682695230078",
        "pn": "1",
        "pz": "500",
        "po": "1",
        "np": "1",
        "fields": "f12,f13,f14,f62",
        "fid": "f62",
        "fs": "m:90+t:2",
        "ut": "b2884a393a59ad64002292a3e90d46a5",
        "_": "1682695230079"
    }
    newR = eastmoney(url, data)
    newR = newR['data']['diff']
    df = pd.DataFrame(newR)
    df = df.loc[:, ['f14', 'f62']]
    new_names = {'f14': '板块', 'f62': '金额'}
    df = df.rename(columns=new_names)
    df['日期'] = today
    df['金额'] = round(df['金额'] / 100000000, 2)

    df.to_sql('板块资金', engine_ts, index=False, if_exists='append', chunksize=5000)


# def futures():
#     # 生猪 ###################
#     url = 'http://futsseapi.eastmoney.com/static/114_lh2209_mx/11?callbackName=jQuery35106817432867056272_1658586689857'
#     result = eastmoney(url)
#     pig = result['mx'][0]['p']
#     content = today + " : " + "生猪2209" + " --> " + str(pig)
#     send_message(content)
#
#     # 黄金 ##################
#     url = "http://futsseapi.eastmoney.com/list/variety/101/1"
#     data = {
#         'callbackName': 'jQuery35109938443184047594_1658587384610',
#         'orderBy': 'zdf',
#         'sort': 'desc',
#         'pageSize': '12',
#         'pageIndex': '0'
#     }
#     result = eastmoney(url, data)
#     gold = result['list'][0]['p']
#     content = today + " : " + "COMEX黄金" + " --> " + str(gold)
#     send_message(content)




# def bitcoin():
#     url = 'https://quotes.sina.cn/fx/api/openapi.php/BtcService.getMinKline?symbol=btcbtcusd&scale=1&datalen=1440' \
#           '&callback=var%20_btcbtcusd_1_1655561443342= '
#
#     result = eastmoney(url)
#     content = "比特币价格" + " : " + result['result']['data'][-1]['d'] + " --> " + result['result']['data'][-1]['c'] + ' USD'
#     send_message(content)


# def wti_oil():
#     url = 'https://stock2.finance.sina.com.cn/futures/api/openapi.php/GlobalFuturesService.getGlobalFuturesMinLine' \
#           '?symbol=CL&callback=var%20t1hf_CL= '
#     result = eastmoney(url)
#     content = "wti_oil" + " : " + result['result']['data']['minLine_1d'][-1][-1] \
#               + " --> " + result['result']['data']['minLine_1d'][-1][1] + " USD"
#     send_message(content)




if __name__ == '__main__':
    #     df = read_data()
    # update_gpList()
    # firstDay = "20230301"
    # days = count_days(firstDay)
    # up_limit(days)
    # query = "SELECT trade_date FROM gp_daily"
    # result = read_data(query)
    # print(result['trade_date'].unique())

    # gp_daily(days)
    # print(today)
    daily_money()
    print("---Finished---")
