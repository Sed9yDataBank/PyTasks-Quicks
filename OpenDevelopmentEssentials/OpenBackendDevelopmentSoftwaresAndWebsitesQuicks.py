"""
Opens All Of The Essentials For Backend Development And Coding Environment
"""

import pyautogui
import webbrowser
import time

webbrowser.open('mozilla')

"""
Checking Cursor Position: print(pyautogui.position())
Opens In My Browser Github, Spring Initializr, Maven Repo For Dependencies, StackOverFlow And Gmail
"""
pyautogui.moveTo(414, 51, duration=1)
pyautogui.click(414, 51)
pyautogui.typewrite("github.com")
pyautogui.typewrite(["enter"])
pyautogui.hotkey("ctrl", "t")
pyautogui.click(414, 51)
pyautogui.typewrite("start.spring.io")
pyautogui.typewrite(["enter"])
pyautogui.hotkey("ctrl", "t")
pyautogui.click(414, 51)
pyautogui.typewrite("mvnrepository.com/repos")
pyautogui.typewrite(["enter"])
pyautogui.hotkey("ctrl", "t")
pyautogui.click(414, 51)
pyautogui.typewrite("stackoverflow.com")
pyautogui.typewrite(["enter"])
pyautogui.hotkey("ctrl", "t")
pyautogui.click(414, 51)
pyautogui.typewrite("gmail.com")
pyautogui.typewrite(["enter"])
pyautogui.click(414, 51)

"""
Opens Spotify, Terminal, Intellij, PostgreSQL, Postman On My Computer
"""

pyautogui.click(271, 1067)
pyautogui.click(427, 1067)
pyautogui.click(523, 1072)

time.sleep(2)
pyautogui.hotkey("ctrl", "shift", "n")
time.sleep(2)
pyautogui.hotkey("ctrl", "o")
