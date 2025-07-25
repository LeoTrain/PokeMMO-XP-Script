import pyautogui, time

def press(key: str, duration: float=0.1):
    pyautogui.keyDown(key)
    time.sleep(duration)
    pyautogui.keyUp(key)

