import pyautogui
import time
import keyboard
import random

time.sleep(5)

number = [1, 2]
bit = [1,2,3,4,5,6,7]
while not keyboard.is_pressed('s'):
    if pyautogui.pixel(1588, 1029)[0] == 119:
        if range(random.choice(number) != 1):
            for i in range(random.choice(bit)):
                print("Ander")
                pyautogui.press('x')
            pyautogui.press('a')
        else:
            for i in range(random.choice(bit)):
                pyautogui.press('z')
            pyautogui.press('b')
