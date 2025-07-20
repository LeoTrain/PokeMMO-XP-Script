from moving_script import Moving
import time
import pyautogui

move = Moving()

def press(key: str, duration: float=0.1):
    pyautogui.keyDown(key)
    time.sleep(duration)
    pyautogui.keyUp(key)

def go_there():
    move.up(1.2)
    move.right(1.8)
    move.down(0.8)
    move.right(5.8)
    move.down(1.5)
    move.right(0.5)
    move.up(3)

def go_back():
    move.down(2.5)
    time.sleep(1.5)
    move.left(0.6)
    move.up(1.5)
    move.left(5.8)
    move.up(0.8)
    move.left(1.8)
    move.down(1.2)

def heal():
    for i in range(10):
        pyautogui.press('j')
        time.sleep(1.2)

def go_to_center():
    time.sleep(3)
    go_there()
    heal()
    go_back()

def use_repell():
    press('b')
    press('down')
    press('j')
    press('j')
    press('k')

def depleat_repell():
    move.left(10)

def go_on_pos():
    move.up(2)
    move.right(1)
    move.up(0.1)

time.sleep(3)
use_repell()
go_on_pos()
depleat_repell()
go_to_center()
