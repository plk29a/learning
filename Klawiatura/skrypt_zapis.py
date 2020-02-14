# -*- coding: cp1250 -*-

import time
import keyboard

#help(mouse)
#help(keyboard)

print('ile rekordów?')

nr_rekord = input()
nr_rekord = int(nr_rekord)


time.sleep(1)
print(3)
time.sleep(1)
print(2)
time.sleep(1)
print(1)
time.sleep(1)
print('go')


liczenie = 1
while liczenie <= nr_rekord:

    time.sleep(0.3)
    keyboard.press_and_release('ctrl + s')
    time.sleep(0.2)
    keyboard.press_and_release('enter')
    time.sleep(0.3)
    keyboard.press_and_release('down')


    print('zapisywanie', liczenie)
    liczenie = liczenie + 1

print('done')
time.sleep(5)
