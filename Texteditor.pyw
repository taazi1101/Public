from tkinter import *
import os

def save(data,files):
    open(files,"wb").write(data.get("0.0",END).encode())

files = os.sys.argv[1]

if os.path.exists(files) == False:
    open(files,"wb").close()

root = Tk()
root.resizable(False,False)
root.title(files)

text_field = Text(width=100,height=35)
text_field.insert(INSERT,open(files,"rb").read())
text_field.grid(row=1,column=0)
save_button = Button(text="Save",width=90,command = lambda:save(text_field,files)).grid(row=0,column=0)


root.mainloop()