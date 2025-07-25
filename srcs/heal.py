from helpers.moving import Move
import time
import pyautogui

def press(key: str, duration: float=0.1):
    pyautogui.keyDown(key)
    time.sleep(duration)
    pyautogui.keyUp(key)

def go_there():
    Move.up(1.2)
    Move.right(1.8)
    Move.down(0.8)
    Move.right(5.8)
    Move.down(1.5)
    Move.right(0.5)
    Move.up(3)

def go_back():
    Move.down(2.5)
    time.sleep(1.5)
    Move.left(0.6)
    Move.up(1.5)
    Move.left(5.8)
    Move.up(0.8)
    Move.left(1.8)
    Move.down(1.2)

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
    Move.left(10)

def go_on_pos():
    Move.up(2)
    Move.right(1)
    Move.up(0.1)

def heal_desert():
    time.sleep(3)
    # use_repell()
    go_on_pos()
    # depleat_repell()
    go_to_center()
    heal()
    go_back()

if __name__ == "__main__":
    heal_desert()
