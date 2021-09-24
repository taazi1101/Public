import threading
from playsound import playsound
from tkinter import *
import time

count = ""

def alert():
    try:
        playsound("alarm.mp3")
    except:
        pass

def conv(num):
    m, s = divmod(num, 60)
    h, m = divmod(m, 60)
    return '{:d}:{:02d}:{:02d}'.format(h, m, s)

def getbutton(root,string):
    global count
    count = string
    root.destroy()

def gettime():
    root = Tk()
    root.title("Select time")
    root.resizable(False,False)
    label = Label(text="Time. (HH.MM.SS)",width=20)
    inp = Entry(width=40)
    button = Button(text="Done",command=lambda:getbutton(root,str(inp.get())),width=35,height=1,background="#E2E7E2")
    label.pack()
    inp.pack()
    button.pack()
    root.mainloop()
    return

def display(label,wait):
    while True:  
        label["text"] = conv(wait)
        label.pack()
        time.sleep(1)
        wait -= 1
        if wait < 0:
            alert()
            return

gettime()

count = count.split(".")
wait = 0
wait += int(count[0])*3600
wait += int(count[1])*60
wait += int(count[2])

tk = Tk()
tk.title("Timer")
tk.resizable(False,False)


label = Label(text="")
label.config(font=('Helvetica bold',80))
threading.Thread(target=lambda:display(label,wait)).start()

tk.mainloop()
