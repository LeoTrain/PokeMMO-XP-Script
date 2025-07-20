import pyautogui
import time

while True:
    time.sleep(1)
    x, y = pyautogui.position()
    color = pyautogui.pixel(401, 180)
    print(f"Position: ({x}, {y})")
    print(f"Couleur RGB: {color}\n")

