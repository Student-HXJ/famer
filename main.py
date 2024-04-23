import pyautogui
import sys
import keyboard
import tkinter as tk
from tkinter import simpledialog

ROOT = tk.Tk()
ROOT.withdraw()

position = simpledialog.askstring(title="输入框", prompt="100,100,100,100")

pyautogui.FAILSAFE = False

poslist = position.split(',')
print(poslist)

if len(poslist) % 2 != 0:
    sys.exit(1)


def mock_click(x, y):
    pyautogui.moveTo(x, y, duration=0.5)
    pyautogui.click()


def mock_write(x, y, content):
    mock_click(x, y)
    pyautogui.write(content, interval=0.25)


def main():
    while(1):
        if keyboard.is_pressed('q'):  # 检测是否按下了'q'键
            print("Exiting...")
            break  # 退出循环
        for i in range(0, len(poslist), 2):
            mock_click(int(poslist[i]), int(poslist[i+1]))

main()

# pyautogui.hotkey('ctrl', 'c')