import pyautogui
import time

class Move():
    def __init__(self) -> None:
        pass

    @staticmethod
    def up(duration: float=0.1):
        pyautogui.keyDown('up')
        time.sleep(duration)
        pyautogui.keyUp('up')

    @staticmethod
    def down(duration: float=0.1):
        pyautogui.keyDown('down')
        time.sleep(duration)
        pyautogui.keyUp('down')

    @staticmethod
    def left(duration: float=0.1):
        pyautogui.keyDown('left')
        time.sleep(duration)
        pyautogui.keyUp('left')

    @staticmethod
    def right(duration: float=0.1):
        pyautogui.keyDown('right')
        time.sleep(duration)
        pyautogui.keyUp('right')
