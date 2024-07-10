import pyautogui
import json
import time
from pynput import keyboard

def on_press(key):
    try:
        if key.char == 'q':
            return False
    except AttributeError:
        pass

class DataHandler:
    def __init__(self):
        pass

    def process_data(self, data):
        data_dict = json.loads(data)
        print(data_dict)
        run_task(data_dict['tasks'])


def mock_click(position, duration=0.5):
    pyautogui.moveTo(position['x'], position['y'], duration=duration)
    pyautogui.click()


def run_task(tasks):
    print("run task num =====> {:d}".format(len(tasks)))
    startTime = time.time()
    if len(tasks) > 0:
        while True:
            if on_press('q'):
                break;
            for task in tasks:
                if time.time() - startTime > task['timeStamp']:
                    for position in task['positions']:
                        mock_click(position, task['duration'])
