import shutil, os
from pathlib import Path
import re

filepath = "/Users/liujiannan/Movies/路飞学城/第三模块/网络编程"
p = Path(filepath)

# 最实用的Python网络编程（完整版）包含所有知识点 - 001 - 20-1 今日概要.mp4
files = p.glob('*')
# pattern = re.compile('(3rd.Rock.from.the.Sun.S\d+E\d+)') --> 要提取的内容
pattern = re.compile('(\d+-\d.*)')
for i in files:
    old = i.name
    # print(old)
    # new = pattern.search(old)[1] + '.mp4'
    new = pattern.search(old)[1]
    # print(new)
    shutil.move(p / old, p / new)

print("Done")