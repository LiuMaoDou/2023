from tkinter import *
from tkinter import messagebox

counter = 0
mark = 1


def pause():
    global mark
    mark = 0


def update_time():
    def counting():
        global counter
        global mark

        counter -= 1
        if counter == 0:
            clock_label.configure(text='...等待下一个番茄钟...', relief="raised", width=19)
            messagebox.showinfo('番茄钟', '...番茄钟结束, 休息一下...')
            return
        clock_label.configure(text=(str(counter) + "s"), relief="raised", width=19)

        if mark == 0:
            messagebox.showinfo('番茄钟', '...番茄钟暂停...')
            mark = 1

        clock_label.after(1000, counting)

    counting()


def timeshow():
    messagebox.showinfo('番茄钟', '...启动番茄钟...')
    global counter
    counter = 1500
    update_time()


def end():
    root.destroy()


root = Tk()
root.title('番茄钟')
root.geometry("210x150+500+300")

btn_start = Button(root, text="启动番茄钟", width=19, command=timeshow)
btn_start.grid(row=0, column=0, columnspan=2, pady=2)

btn_pause= Button(root, text="暂停番茄钟", width=19, command=pause)
btn_pause.grid(row=1, column=0, columnspan=2, pady=2)

btn_end = Button(root, text="结束番茄钟", width=19, command=end)
btn_end.grid(row=2, column=0, columnspan=2, pady=2)

clock_label = Label(root)
clock_label.grid(row=3, column=0, columnspan=2, pady=2)

root.mainloop()
