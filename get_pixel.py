import pyautogui
import time

PIXEL_POS = (731, 180)
PIXEL_POS_TRIO = (867, 131)
PIXEL_POS_MON_BAR = (1260, 465)
PIXEL_COLOR_MON_BAR_ORANGE = (211, 211, 211, 255)
PIXEL_COLOR_MON_BAR_RED = (155, 155, 155, 255)
PIXEL_COLOR_LIFE_BAR = (253, 253, 253, 255)

def is_color_close(c1: tuple, c2: tuple, tolerance: float=10):
    print(f"Checking if {c1} is close to {c2}...")
    return all(abs(a - b) <= tolerance for a, b in zip(c1[:3], c2[:3]))

def get_pixel(pixel_pos: tuple) -> float | tuple[int,...] | None:
    print(f"Getting pixel on pos ({pixel_pos[0]},{pixel_pos[1]}).")
    screenshot = pyautogui.screenshot(region=(pixel_pos[0], pixel_pos[1], 1, 1))
    return screenshot.getpixel((0, 0))

while True:
    time.sleep(1)
    x, y = pyautogui.position()
    color = get_pixel((x, y))
    print(f"Position: ({x}, {y})")
    print(f"Couleur RGB: {color}")
    # print(is_color_close(color, PIXEL_COLOR_MON_BAR_ORANGE))
    print()



