import keyboard
import threading
import time
import os

def check(key,kill):
    while True:
        if keyboard.is_pressed(key):
            os.system("taskkill /im "+kill+".exe /f")
            os.system("taskkill /im "+kill+" /f")
            os.system("taskkill /im "+os.path.basename(kill)+" /f")
            os.system("taskkill /im "+os.path.basename(kill)+".exe /f")
            break
        time.sleep(0.01)

key = "space"

program = input("Program\n:")
kill = input("Process name (Leave empty to use program name)\n:")
if len(kill) < 1:
    kill = program.split(" ")[0]

threading.Thread(target=lambda:check(key,kill)).start()
os.system(program)
