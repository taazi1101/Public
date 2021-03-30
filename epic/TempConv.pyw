from tkinter import *

win = Tk()
win.title("")
win.resizable(False, False)

entry = Entry(width=32)
entry.grid(row=1, column=0)


def FToC():
    result = (float(entry.get()) - 32) * 5/9
    entry.delete(0, END)
    entry.insert(0, str(round(result, 2)))

def CToF():
    result = float(entry.get()) * 9/5 + 32
    entry.delete(0, END)
    entry.insert(0, str(round(result, 2)))

def ctok():
    result = float(entry.get()) + 273.15
    entry.delete(0, END)
    if result < 0:
        entry.insert(0, "Kelvin cannot be negative")
        return
    entry.insert(0, str(round(result, 2)))

def ktoc():
    if float(entry.get()) < 0:
        entry.delete(0, END)
        entry.insert(0, "Kelvin cannot be negative")
        return
    result = float(entry.get()) - 273.15
    entry.delete(0, END)
    entry.insert(0, str(round(result, 2)))

ftoc_button = Button(text="°F To °C", padx=77, pady=10, command=FToC)
ctof_button = Button(text="°C To °F", padx=77, pady=10, command=CToF)
ctok_button = Button(text="°C to °K", padx=77, pady=10, command=ctok)
ktoc_button = Button(text="°K to °C", padx=77, pady=10, command=ktoc)

ktoc_button.grid(row=6, column=0)
ctok_button.grid(row=5, column=0)
ftoc_button.grid(row=3, column=0)
ctof_button.grid(row=4, column=0)

win.mainloop()
