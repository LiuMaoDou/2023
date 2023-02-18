from PIL import Image, ImageGrab
from aip import AipOcr  # baidu-aip
import os
import pyperclip

APP_ID = '21808493'
API_KEY = 'xXUZ0xzi2b7LQgwoYilrulBE'
SECRET_KEY = 'LxyP9CP6uUUGAXKq62mMRd6IAEed7hYA'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

temp_pic = '/Users/liujiannan/Desktop/temp_pic_xx.png'

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


if __name__ == "__main__":
    # pic = '/Users/liujiannan/Desktop/iShot_2023-01-14_00.30.04.png'
    pic = ImageGrab.grabclipboard()
    pic.save(temp_pic)
    image = get_file_content(temp_pic) 
    text = client.basicAccurate(image) # basicGeneral

    xxy = ""
    result = text["words_result"]
    for i in result:
        xxy += (i["words"] + "\n")
        # print(i["words"])
        # print('\n')
        # lst.append(i['words'])
    print(xxy)
    pyperclip.copy(xxy)

