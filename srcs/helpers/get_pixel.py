import pyautogui
import time

def is_color_close(c1: tuple, c2: tuple, tolerance: float=10):
    print(f"Checking if {c1} is close to {c2}...")
    return all(abs(a - b) <= tolerance for a, b in zip(c1[:3], c2[:3]))

def get_pixel(pixel_pos: tuple) -> float | tuple[int,...] | None:
    print(f"Getting pixel on pos ({pixel_pos[0]},{pixel_pos[1]}).")
    screenshot = pyautogui.screenshot(region=(pixel_pos[0], pixel_pos[1], 1, 1))
    return screenshot.getpixel((0, 0))
