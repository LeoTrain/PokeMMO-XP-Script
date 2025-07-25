from helpers import *

class XpBot():
    def __init__(self) -> None:
        self.log = True
        self.current_log = ""
        self.needs_healing = False

    def _log(self, msg: str, timer=None) -> None:
        if self.log and not timer:
            self.current_log = msg
            print(msg, flush=True)
        elif self.log and timer:
            self.current_log = msg
            for i in reversed(range(timer)):
                nbr = f"{i + 1}..."
                self.current_log = f"{msg}{''.join(nbr)}"
                print(self.current_log, flush=True)
                time.sleep(1)
        elif not self.log and timer:
            time.sleep(timer)

    def _is_in_battle(self):
        self._log("Checking if is in a normal battle...")
        color = get_pixel(PIXEL_POS)
        return is_color_close(color, PIXEL_COLOR_LIFE_BAR)

    def _is_in_trio_battle(self):
        self._log("Checking if is in a trio battle...")
        color = get_pixel(PIXEL_POS_TRIO)
        return is_color_close(color, PIXEL_COLOR_LIFE_BAR)

    def _is_needing_healing(self):
        self._log("Checking if 'mon needs healing...")
        color = get_pixel(PIXEL_POS_MON_BAR)
        self.needs_healing = True
        return is_color_close(color, PIXEL_COLOR_MON_BAR_ORANGE) and is_color_close(color, PIXEL_COLOR_MON_BAR_RED)

    def _move(self, tiles: int=5):
        self._log("Moving up and down...")
        for _ in range(tiles):
            Move.up()
        for _ in range(tiles):
            Move.down()

    def _battle(self):
        self._log(msg="Waiting for battle to start: ", timer=15)
        while self._is_in_battle():
            for _ in range(10):
                pyautogui.press('up')
                pyautogui.press('left')
            for _ in range(2):
                pyautogui.press('j')
            self._log(msg="Waiting for battle to end: ", timer=15)

    def _skip_battle(self):
        pyautogui.press('down')
        pyautogui.press('right')
        pyautogui.press('j')

    def run(self):
        # self._log("Starting XpBot in ", timer=3)
        self._log("Step 0: Focusing app:")
        if not focus():
            return
        while True:
            self._log("Step: 1 - Moving:")
            while not self._is_in_battle() and not self._is_in_trio_battle():
                self._move()
            self._log("Step: 2 - Batteling:")
            if self._is_in_battle():
                self._battle()
            elif self._is_in_trio_battle():
                self._skip_battle()

bot = XpBot()
bot.run()
