import efinance as ef
import webbrowser
import requests
from tkinter import messagebox


df = ef.stock.get_realtime_quotes()
random = df.sample(1)
value = random.at[random.index[0], random.columns[0]]
# value =  "002967"

url = "http://www.iwencai.com/unifiedwap/result?w={}".format(value)
webbrowser.open(url)
url = 'https://t.10jqka.com.cn/newcircle/group/modifySelfStock/?callback=modifyStock&op=add&stockcode={}'.format(value)

cookie = "Hm_lvt_722143063e4892925903024537075d0d=1682756925; Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1682756925; " \
         "u_dpass=V8NZYbhbQXPzdwidJ3kUNXr3LHsbYc31lRk6KHeaWaGF0VVHe1UHfthcBhs%2BNREP%2FsBAGfA5tlbuzYBqqcUNFA%3D%3D; " \
         "u_did=7932943759ED47A5B503E42319475C58; u_ttype=WEB; u_ukey=A10702B8689642C6BE607730E11E6E4A; u_uver=1.0.0; " \
         "user=MDptb180MTYwOTcwMTY6Ok5vbmU6NTAwOjQyNjA5NzAxNjo3LDExMTExMTExMTExLDQwOzQ0LDExLDQwOzYsMSw0MDs1LDEsNDA7MSwxMDEsNDA7MiwxLDQwOzMsMSw0MDs1LDEsNDA7OCwwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMSw0MDsxMDIsMSw0MDoyNDo6OjQxNjA5NzAxNjoxNjgyNzU2OTU5Ojo6MTUwNjQ2NTkwMDo4NjQwMDowOjE4YWVjNGEwMWNlYjFmMWQ0OTQzNTNiZmViMGY4MWZmMjpkZWZhdWx0XzQ6MQ%3D%3D; userid=416097016; u_name=mo_416097016; escapename=mo_416097016; ticket=857c8f1cdc49dc090fd57829c895a7d8; user_status=0; utk=96a882253aa677493e40acde06c5ac78; Hm_lvt_da7579fd91e2c6fa5aeb9d1620a9b333=1682756996; __bid_n=187cc2669b036faab84207; FPTOKEN=PvpmWlZzJAw7wi3gJws6v+bbqI5fCzObaju5v5uVeIouviN1uVzut0YdOSqJ2QtqXCzo9vwsI64uCZzKjB2CKsUdLeThss1LOKe4McuT6Nfm+syIURQJifCGHnWuXpO1Cr85Sgfq6DPWuzTja4VOL1yOorHKN90kBWF3T0xABjg6MrijBHg13QJWTWQw4VZqOJ0H7QPSx1n+3sikVKA5/lMCGA+Mh+7mffJm2ohyFp4P9sEiMbxI8c6CiYuCoS9qGlQMZSqBsXTS+KYWy5ZFDwv26xz3Nvpixr3Cjzgkgmhgmt0qqZfP6v8Nsz8osTyJqieATQIQju+uHLlW369QYfwftMJA2ejwd7cR8fXyjwniXrnXc/mNSaH7Nw1R5ZLV8fdnDmZVR/Ian4UhzBqP3g==|Wbmog7QU0gU1hoWpgMvx755014I4rLQJ2ZwuGxybO9w=|10|1be9b93f4fac6c8a39a78e55fbcac778; __utma=156575163.1580449947.1682757283.1682757283.1682757283.1; __utmc=156575163; __utmz=156575163.1682757283.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); Hm_lpvt_722143063e4892925903024537075d0d=1682827125; log=; Hm_lpvt_da7579fd91e2c6fa5aeb9d1620a9b333=1682827132; Hm_lpvt_78c58f01938e4d85eaf619eae71b4ed1=1682827132; v=A8DJahFYsM4Q5UzKDdf6ICHql0WXSaUkRin4FzpTiOJuOm574ll0o5Y9yKqJ"
headers = {'cookie': cookie, "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
requests.get(url=url, headers=headers)

url = "https://t.10jqka.com.cn/newcircle/user/userPersonal/?from=finance&tab=zx###"
webbrowser.open(url)


url = "https://zhujia.zhuwang.cc/"
webbrowser.open(url)

url = "http://quote.eastmoney.com/globalfuture/CL00Y.html"
webbrowser.open(url)

url = "http://quote.eastmoney.com/globalfuture/GC00Y.html"
webbrowser.open(url)

url = "https://data.eastmoney.com/bkzj/hy.html"
webbrowser.open(url)

messagebox.showinfo('提示', '结束')
