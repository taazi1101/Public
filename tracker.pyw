from tkinter import *

def reset(target):
    global valies
    valies = 0
    target.delete(0,END)
    target.insert(0,str(valies))
    open("val.save","w").write(str(valies))

def add(num,num2,target):
    global valies
    num = int(num.replace(" ",""))
    num2 = int(num2)
    valies =  num + num2
    target.delete(0,END)
    target.insert(0,str(valies))
    open("val.save","w").write(str(valies))

try:
    valies = int(open("val.save","r").read())
except:
    valies = 0

tk = Tk()
tk.title("Tracker")
tk.resizable(False,False)
rset = Button(text="Reset",command =lambda:reset(val_show),width = 10)
entr = Entry(tk,width=10)
val_add = Button(text="Add",command = lambda:add(entr.get(),valies,val_show),width=10)
val_show = Entry(tk,width=10)
val_show.insert(0,str(valies))

entr.grid(row=0,column=0)
val_show.grid(row=0,column=1)
val_add.grid(row=1,column=0)
rset.grid(row=1,column=1)


tk.mainloop()