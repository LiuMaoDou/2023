import efinance as ef
import pandas as pd
import os
import datetime
import xlwings as xw

os.chdir('/Users/liujiannan/Desktop/')
today = datetime.date.today().strftime('%Y%m%d')


# 财报信息
# ef.stock.get_all_company_performance()

data = ef.stock.get_realtime_quotes()
filename = today+'-A股.xlsx'
data.to_excel(filename)
wb = xw.Book(filename)
sheet = wb.sheets.active
sheet.autofit()
