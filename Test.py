import random 

import pyautogui as pg 

import time

animal = ('biss','boss','bus','baby','babu','bsdk')

time.sleep(8)

for i in range (500):

    a = random.choice(animal)
    pg.write(a)

    pg.press('enter')

