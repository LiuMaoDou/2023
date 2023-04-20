import requests
from lxml import etree
import json


cookie = "device_id=57caf4a91ce6ff9c55bbc46a921c7cf9; Hm_lvt_1db88642e346389874251b5a1eded6e3=1679186533,1680297823,1680354558,1680358955; acw_tc=2760828016816634535552305e8f02be55364c22c376a09d0891168c7d9301; s=am12kuvgmd; xq_a_token=f4b52676bbad3e8e59c0276a962c3f2d751b6479; xqat=f4b52676bbad3e8e59c0276a962c3f2d751b6479; xq_r_token=433d94833743dc84d8054f523ff7d5c356ca2ca1; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOjEyMzE0NjE3NTEsImlzcyI6InVjIiwiZXhwIjoxNjg0MjU1NDQ0LCJjdG0iOjE2ODE2NjM0NzI2NDUsImNpZCI6ImQ5ZDBuNEFadXAifQ.FOyAvnv1HF-PYr17F9267EbqdlINPzEDafxdwFf8MDKKXYydrILuyOm8c19SfzmNEnx70OlEk04nIokuGdo9MA_nd7d3tPHrKFiyroieIHnOmuRi2ypYTuXhFBO5JQc5l6Vj9Pp6TSyswoRRnYKkjVJZLEldk3A61J4ap_vnMUrdnTZo8ipPG8H230Jb-CugPi331xHKI_p0YfXhMjmI-00_HSEHUvPMbrX5rhAZklDOlvjw1uUBcCFHjT8a2LWqlS4NyI3yuHuAOtoboCurAb-FR_8H2L2HwcJ1V2WPQSn5BTDCJyIExtBfYbg8p62ibzzFEmmZwTh-W7amwS_eTQ; xq_is_login=1; u=1231461751"

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
