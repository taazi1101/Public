from selenium import webdriver
import ast
import base64
import os

def openpr_ff(url,cookies,private):
    options = webdriver.FirefoxOptions()
    if private:
        options.add_argument("--private")
    browser = webdriver.Firefox(options=options)
    browser.get(url)
    for x in cookies: 
        browser.add_cookie(x)
    browser.refresh()

def openpr_ch(url,cookies,private):
    options = webdriver.ChromeOptions()
    if private:
        options.add_argument("--incognito")
    browser = webdriver.Chrome(options=options)
    browser.get(url)
    for x in cookies: 
        browser.add_cookie(x)
    browser.refresh()
    

def new_preset(name):
    url = input("Url\n:")
    print("Chrome:1 | Firefox:2")
    borw = input(":")
    is_priv = input("Private y/n\n:")

    if borw == "1":
        options = webdriver.ChromeOptions()
        if is_priv == "y":
            options.add_argument("--incognito")
        browser = webdriver.Chrome(options=options)
        browser.get(url)
    elif borw == "2":
        options = webdriver.FirefoxOptions()
        if is_priv == "y":
            options.add_argument("--private")
        browser = webdriver.Firefox(options=options)
        browser.get(url)

    input("Set cookies and then press enter twice.")
    cookies = browser.get_cookies()

    data = f"{url}\n{cookies}".encode()

    data = base64.encodebytes(data)

    with open("Presets/"+name,"wb") as fil:
        fil.write(data)

mode = input("Open preset:1 | New preset:2\n:")
name = input("Preset name\n:")

try:
    os.mkdir("Presets")
except:
    pass

if mode == "2":
    new_preset(name)
else:
    with open("Presets/"+name,"rb") as fil:
        data = base64.decodebytes(fil.read()).decode().split("\n")
    
    cok = data[1]
    cookies = ast.literal_eval(cok)

    print("Chrome:1 | Firefox:2")
    borw = input(":")
    is_priv = input("Private y/n\n:")
    print("If the cookies didin't load refresh the page.")
    if borw == "1":
        openpr_ch(data[0],cookies,is_priv == "y")
    else:
        openpr_ff(data[0],cookies,is_priv == "y")

input()
