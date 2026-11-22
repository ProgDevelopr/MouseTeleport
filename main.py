"""MsTp Code - V1"""

from pyautogui import position, moveTo, size
from keyboard import is_pressed as p
from time import sleep
from sys import exit

condition_save = lambda: p("esc") and p("shift")
condition_move = lambda: p("esc") and p("alt")

move_x, move_y = size()[0]//2, size()[-1]//2
while True:
    try:
        if condition_save():
            move_x, move_y = position()
            print(f"X: {move_x}, Y: {move_y}")
            sleep(0.2)
        if condition_move():
            print(f"Moved cursor to ({move_x}, {move_y}).")
            moveTo(move_x, move_y)
            sleep(0.2)
    except KeyboardInterrupt:
        exit(0)
        break
