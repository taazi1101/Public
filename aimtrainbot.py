# Name picture with target "target.png"

import pyautogui
import keyboard
import time

def pause():
    print("Press w to continue.")
    time.sleep(1.5)
    while True:
        if keyboard.is_pressed("w"):
            return
        time.sleep(0.1)

delay = float(0.01)
pyautogui.PAUSE = 0

topleft = ()
downright = ()

print("Press k on top of top left corner")
while True:
    if keyboard.is_pressed("k"):
        topleft = pyautogui.position()
        break
    time.sleep(0.1)
time.sleep(1)
print("Press k on top of top bottom right")
while True:
    if keyboard.is_pressed("k"):
        downright = pyautogui.position()
        break
    time.sleep(0.1)


print("Press shift to start.")
while keyboard.is_pressed("shift") == False:
    time.sleep(0.1)
print("Press q to quit. Press w to pause")

while True:
    try:
        x = pyautogui.locateOnScreen("target.png",grayscale=True,confidence=0.35,region=(topleft[0],topleft[1],downright[0],downright[1]))
        if x != None:
            pyautogui.click(pyautogui.center(x))

        if keyboard.is_pressed("q"):
            exit()
        if keyboard.is_pressed("w"):
            pause()
        time.sleep(delay)
    except:
        raise
        print("Error press q to exit.")
        if keyboard.is_pressed("q"):
            exit()
        continue
