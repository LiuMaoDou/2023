from tkinter import *
from tkinter import messagebox
import time, datetime
import pandas as pd
import xlwings as xw


def update_time():
    clock_label.configure(text=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), font="微软雅黑")
    clock_label.after(1000, update_time)


def task_input():
    global count

    task_value = task_txt.get()
    task_txt.delete(0, END)

    task_value_son = task_txt_son.get()
    task_txt_son.delete(0, END)

    start = time.time()
    start1 = datetime.datetime.now()
    start2 = start1.strftime('%Y/%m/%d %H:%M:%S')

    messagebox.showinfo('任务', '结束任务')

    end = time.time()
    end1 = start1 + datetime.timedelta(seconds=end - start)
    end2 = end1.strftime('%Y/%m/%d %H:%M:%S')
    lst = [task_value, task_value_son, start2, end2, str(round(end - start)), str(round((end - start) / 60))]
    location = "A" + str(count)
    sheet.range(location).value = lst
    sheet.autofit(axis="columns")
    wb.save(expath)
    count += 1

def stop_task():
    messagebox.showinfo('结束', '======今天任务结束======')
    root.destroy()


if __name__ == '__main__':
    count = 2
    filename = datetime.datetime.now().strftime('%Y-%m-%d-%H')
    expath = "/Users/liujiannan/Desktop/时间管理/" + filename + ".xlsx"
    last = {}
    last.setdefault("", ["", "", "", "", ""])
    frame = pd.DataFrame.from_dict(last, orient="index").reset_index().rename(columns={
        'index': "任务", 0: "子任务", 1: "Start_Time", 2: "End_Time", 3: "Duration", 4: "Mins"
    })
    frame.to_excel(expath, index=False)
    wb = xw.Book(expath)
    sheet = wb.sheets['Sheet1']

    root = Tk()
    root.title('时间管理')
    root.geometry('400x150+500+300')

    task_txt = Entry(root, width=15, font="微软雅黑")
    task_txt.grid(row=1, column=1)

    task = Button(root, text="主任务", width=15, font="微软雅黑", command=task_input)
    task.grid(row=1, column=0)

    task_txt_son = Entry(root, width=15, font="微软雅黑")
    task_txt_son.grid(row=2, column=1)

    task = Button(root, text="子任务", width=15, font="微软雅黑")
    task.grid(row=2, column=0)

    stop = Button(root, text="终止", width=15, font="微软雅黑", command=stop_task)
    stop.grid(row=3, column=0)

    clock_label = Label(root)
    clock_label.grid(row=3, column=1)
    update_time()

    root.mainloop()
