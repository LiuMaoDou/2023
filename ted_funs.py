import tkinter as tk
from tkinter import filedialog
import requests
import re
import json
import pandas as pd
import datetime
today = datetime.date.today().strftime('%Y%m%d')


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

