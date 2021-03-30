from tkinter import *

root = Tk()
root.resizable(False, False)
root.title("")

def mtof():
    result = float(entry.get()) / 0.3048
    entry.delete(0, END)
    entry.insert(0, round(result, 1))

def ftom():
    result = float(entry.get()) * 0.3048
    entry.delete(0, END)
    entry.insert(0, round(result, 1))

entry = Entry(width=25)
mtof_button = Button(text="Meters To Feet", padx=39, pady=10, command=mtof)
ftom_button = Button(text="Feet to Meters", padx=40, pady=10, command=ftom)

entry.grid(row=0, column=0)
mtof_button.grid(row=1, column=0)
ftom_button.grid(row=2, column=0)

root.mainloop()