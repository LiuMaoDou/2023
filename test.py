import os
import tkinter as tk
from tkinter import filedialog

def input_folder_path():
    window = tk.Tk()
    window.title('(^_^))')
    window.geometry('220x20')
    tk.Label(window, text='"Pls Select The File"').pack()
    inpath = filedialog.askdirectory()
    window.destroy()
    return inpath


print(input_folder_path())
