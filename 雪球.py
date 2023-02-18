import requests
from lxml import etree
import json


cookie = 'evice_id=57caf4a91ce6ff9c55bbc46a921c7cf9; s=bx1ibstrvx; bid=5d8b60fc18b8293ee2bd1aae2669da33_lcnfpqde; cookiesu=801673186224382; __utma=1.1613440696.1673185953.1673185953.1673186705.2; __utmz=1.1673186705.2.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); remember=1; xq_is_login=1; u=1231461751; xq_a_token=3399facea4eef0a881c677237e2802dbe4e62f1a; xqat=3399facea4eef0a881c677237e2802dbe4e62f1a; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOjEyMzE0NjE3NTEsImlzcyI6InVjIiwiZXhwIjoxNjc3MzM2MDkyLCJjdG0iOjE2NzQ3NDQwOTIwMjMsImNpZCI6ImQ5ZDBuNEFadXAifQ.V3uHuuq0k0CqdlvG59u2kOWsFA3Dm_gckiZPMPtDe90uJ99m9pw8sp2NzeGzp0y3BBVuU450OpS2AxP2gwckzGc0XL4JmLVsJRBlScAZhcf3ns3yQ2zV48Ms8gFGzUbIFWzRnBci-bC4tetHbHXxCnIflWca3yQS0-RF7mDVCuDoq3KfL2hHPpwEHTGRCqRplxiRAdodU-cffDT8391xZXmlDKRwauHX0jXEmysLK-PCPPB1jsxEkqw8PCq8x5Tl6b3_KZ-fcUUP4Ce5PPZry3sPrIkp5K-8WtTKiGsHO0Y-COy7WnZo00nG-ewHug8IeeHKGeVMdl8aeTr4Om-7SQ; xq_r_token=94f735a79efe3032906aabc20491ccfccbd53fe7; Hm_lvt_1db88642e346389874251b5a1eded6e3=1673185149,1673359095,1673876462,1674744093; acw_tc=276077b616747459486952759e41c80f14533e16ceab886a63fb6bffb1ffff; snbim_minify=true; is_overseas=0; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1674747652'

headers = {'cookie': cookie, "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}


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
