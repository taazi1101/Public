import pyautogui
import keyboard
import time

delay = float(0.01)
onepress = False
compensation = True
pyautogui.PAUSE = 0
keyspr = 0
keypos = []
print("Press k on top of all tiles left to right.")
while keyspr != 4:
    if keyboard.is_pressed("k"):
        keypos.append(pyautogui.position())
        keyspr += 1
        time.sleep(0.2)
    
print("Press shift to start.")
while keyboard.is_pressed("shift") == False:
    time.sleep(0.1)
print("Press q to quit.")

lastpos = ()
redun = 0
x = 0

while True:
    for pos in keypos:
        try:
            if onepress and pos == lastpos:
                pass
            else:
                if pyautogui.pixelMatchesColor(int(pos[0]),int(pos[1]-redun),(0,0,0),tolerance=30):
                    pyautogui.click(pos)
                    lastpos = pos
                    x += 1
            if compensation:
                if x > 60 and redun < 500:
                    redun += 1
                    x = 0
            if keyboard.is_pressed("q"):
                exit()
            time.sleep(delay)
        except:
            print("Error press q to exit.")
            if keyboard.is_pressed("q"):
                exit()
            continue
