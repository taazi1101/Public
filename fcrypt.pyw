import tkinter as tk
from cryptography import fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import hashlib
import os
import base64
import threading
from tkinter import *
import tkinter.filedialog as fd

def get_filez(root,listbox):
    global filez
    filez = fd.askopenfilenames(parent=root, title='Choose a file')
    for values in filez:
        listbox.insert(END, values)
    return

def clear(listbox):
    listbox.delete(0,END)

def encrypt(root,filez,pas):
    txt = Label(root,text="")
    salt = b'Y&\x8c/O@\x9d*\xc9\xe3\x1a?Z\x9b\x9a\xbe'
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000
    )
    key = base64.urlsafe_b64encode(kdf.derive(pas.encode()))
    f = fernet.Fernet(key)
    for fil in filez:
        try:
            txt["text"] = fil
            txt.grid(row=5,column=0,columnspan=2)
            with open(fil,"rb") as file:
                data = file.read()
                enc = f.encrypt(data)
            with open(fil,"wb") as file:
                file.write(enc)
        except:
            txt["text"] = "Error Encrypting: " + fil
            txt.grid(row=5,column=0,columnspan=2)
            pass
    txt["text"] = "Done"
    txt.grid(row=5,column=0,columnspan=2)
    return

def decrypt(root,filez,pas):
    salt = b'Y&\x8c/O@\x9d*\xc9\xe3\x1a?Z\x9b\x9a\xbe'
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000
    )
    key = base64.urlsafe_b64encode(kdf.derive(pas.encode()))
    f = fernet.Fernet(key)
    txt = Label(root,text="")
    for fil in filez:
        try:
            txt["text"] = fil
            txt.grid(row=5,column=0,columnspan=2)
            with open(fil,"rb") as file:
                data = file.read()
                enc = f.decrypt(data)
            with open(fil,"wb") as file:
                file.write(enc)
        except:
            txt["text"] = "Error Decrypting: " + fil
            txt.grid(row=5,column=0,columnspan=2)
            pass
    txt["text"] = "Done"
    txt.grid(row=5,column=0,columnspan=2)
    return

root = tk.Tk()
root.resizable(False,False)
filez = []
pass_label = Label(text="Password")
pass_entry = Entry(width=50)
listbox = Listbox(root,width=50)

sele = Button(text="Select files",width=20,command = lambda:get_filez(root,listbox))
act1 = Button(text="Encrypt",width=20,command = lambda:threading.Thread(target=lambda:encrypt(root,filez,pass_entry.get())).start())
act2 = Button(text="Decrypt",width=20,command = lambda:threading.Thread(target=lambda:decrypt(root,filez,pass_entry.get())).start())
clea = Button(text="Clear",width=20,command=lambda:clear(listbox))

pass_label.grid(row=0,column=0,columnspan=2)
pass_entry.grid(row=1,column=0,columnspan=2)
act1.grid(row=2,column=0)
act2.grid(row=2,column=1)
listbox.grid(row=3,column=0,columnspan=2)
sele.grid(row=4,column=0)
clea.grid(row=4,column=1)


root.mainloop()
