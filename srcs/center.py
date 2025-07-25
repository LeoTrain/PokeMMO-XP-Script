import time
from helpers import Move, press, focus

def go_on_pos_woods():
    Move.up(2)
    Move.right(1)
    Move.up(0.1)

def go_on_pos_desert():
    Move.up(2)
    Move.right(0.1)
    Move.up(1.9)
    Move.left(1)
    Move.up(2.2)
    Move.left(0.1)
    Move.up(0.05)
    Move.left(0.05)
    press('j')
    time.sleep(1)
    press('j')
    time.sleep(3)
    Move.down(0.1)
    Move.right(0.1)
    Move.down(2)
    Move.right(0.5)
    Move.down(2)
    Move.left(0.2)

if __name__ == "__main__":
    focus()
    go_on_pos_desert()
