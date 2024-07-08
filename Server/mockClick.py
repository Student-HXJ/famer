import pyautogui
import json
import time

class DataHandler:
    def __init__(self):
        pass

    def process_data(self, data):
        data_dict = json.loads(data)
        run_task(data_dict)


def mock_click(position, duration=0.5):
    pyautogui.moveTo(position['x'], position['y'], duration=duration)
    pyautogui.click()


def run_task(tasks):
    print("run task num =====> {:d}".format(len(tasks)))
    if len(tasks) > 0:
        while True:
            startTime = time.time()
            for task in tasks:
                if time.time() - startTime > task['timeStamp']:
                    for position in task['positions']:
                        mock_click(position, task['duration'])
