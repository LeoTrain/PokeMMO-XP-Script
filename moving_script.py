import mss
import pyautogui
import time
from PIL import Image
from AppKit import NSWorkspace
import subprocess

PIXEL_POS = (731, 180)
PIXEL_POS_TRIO = (867, 131)
PIXEL_COLOR_LIFE_BAR = (253, 253, 253, 255)

class Moving():
    def __init__(self) -> None:
        pass

    def up(self, duration: float=1.0):
        pyautogui.keyDown('up')
        time.sleep(duration)
        pyautogui.keyUp('up')

    def down(self, duration: float=1.0):
        pyautogui.keyDown('down')
        time.sleep(duration)
        pyautogui.keyUp('down')

    def left(self, duration: float=1.0):
        pyautogui.keyDown('left')
        time.sleep(duration)
        pyautogui.keyUp('left')

    def right(self, duration: float=1.0):
        pyautogui.keyDown('right')
        time.sleep(duration)
        pyautogui.keyUp('right')

class XpBot():
    def __init__(self) -> None:
        self._mover = Moving()

    def _focus_pokemmo(self):
        app_name = "java"
        ws = NSWorkspace.sharedWorkspace()
        apps = ws.runningApplications()
        for app in apps:
            if app.localizedName() == app_name:
                app.activateWithOptions_(1 << 1)
                time.sleep(0.5)
                print("App found but not focused, trying to click...")
                subprocess.run([
                    "osascript", "-e",
                    'tell application "System Events" to tell process "java" to set frontmost to true'
                ])
                subprocess.run([
                    "osascript", "-e",
                    'tell application "System Events" to click at {800, 300}'
                ])
                return True
        print("PokeMMO app not found.")
        return False

    def _is_color_close(self, c1: tuple, c2: tuple, tolerance: float=10):
        return all(abs(a - b) <= tolerance for a, b in zip(c1[:3], c2[:3]))

    def _get_pixel(self, pixel_pos: tuple):
        screenshot = pyautogui.screenshot(region=(pixel_pos[0], pixel_pos[1], 1, 1))
        return screenshot.getpixel((0, 0))

    def _is_in_battle(self):
        color = self._get_pixel(PIXEL_POS)
        print(f"Color read: {color}")
        return self._is_color_close(color, PIXEL_COLOR_LIFE_BAR)

    def _is_in_trio_battle(self):
        color = self._get_pixel(PIXEL_POS_TRIO)
        print(f"Color read: {color}")
        return self._is_color_close(color, PIXEL_COLOR_LIFE_BAR)

    def _move(self, duration: float=0.5):
        self._mover.up(duration)
        self._mover.down(duration)

    def _battle(self):
        time.sleep(15)
        while self._is_in_battle():
            for _ in range(10):
                pyautogui.press('up')
                pyautogui.press('left')
            for _ in range(2):
                pyautogui.press('j')
            time.sleep(15)

    def _skip_battle(self):
        pyautogui.press('down')
        pyautogui.press('right')
        pyautogui.press('j')

    def run(self):
        time.sleep(5)
        if not self._focus_pokemmo():
            return
        while True:
            print("Step: 1 - Moving:")
            while not self._is_in_battle() and not self._is_in_trio_battle():
                self._move()
            print("Step: 2 - Batteling:")
            if self._is_in_battle():
                self._battle()
            elif self._is_in_trio_battle():
                self._skip_battle()

def main():
    bot = XpBot()
    bot.run()

if __name__ == "__main__":
    main()

