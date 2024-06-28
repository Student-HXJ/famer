import pyautogui
import sys
import keyboard
import tkinter as tk
from tkinter import simpledialog
import time

# 初始化Tkinter
ROOT = tk.Tk()
ROOT.withdraw()

# 获取用户输入的坐标
def get_coordinates(prompt):
    position = simpledialog.askstring(title="输入框", prompt=prompt)
    return [int(coord) for coord in position.split(',')]

# 获取八个坐标
def get_multiple_coordinates(prompt):
    positions = simpledialog.askstring(title="输入框", prompt=prompt)
    coords = positions.split(';')
    return [[int(coord) for coord in pos.split(',')] for pos in coords]

# 获取八个坐标
coordinates = get_multiple_coordinates("请输入八个坐标 (格式: x1,y1;x2,y2;...;x8,y8):")

# 获取关闭坐标
close_coord = get_coordinates("请输入关闭坐标 (格式: x,y):")

# 获取鼠标移动的时间间隔
mouse_time = simpledialog.askfloat("输入框", "请设置鼠标移动的时间间隔（秒）:")

# 获取背包坐标
backpack_coord = get_coordinates("请输入背包坐标 (格式: x,y):")

# 获取补充能量坐标
energy_coord = get_coordinates("请输入补充能量坐标 (格式: x,y):")

# 获取时间间隔
time_interval = simpledialog.askinteger("输入框", "请输入时间间隔（秒）:")

pyautogui.FAILSAFE = False

def mock_click(x, y):
    pyautogui.moveTo(x, y, duration=float(mouse_time))
    pyautogui.click()

def recover_energy():
    mock_click(backpack_coord[0], backpack_coord[1])
    mock_click(energy_coord[0], energy_coord[1])

def click_desk(coord):
    mock_click(coord[0], coord[1])
    mock_click(close_coord[0], close_coord[1])

def main():
    start_time = time.time()
    while True:
        if keyboard.is_pressed('q'):  # 检测是否按下了'q'键
            print("Exiting...")
            break  # 退出循环
        for coord in coordinates:
            click_desk(coord)
            if keyboard.is_pressed('q'):  # 再次检查以便在点击操作中能够及时响应
                print("Exiting...")
                return  # 退出函数
        if time.time() - start_time >= time_interval:
            recover_energy()
            start_time = time.time()  # 重置计时器

if __name__ == "__main__":
    main()