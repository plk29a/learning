# -*- coding: cp1250 -*-
import time
import keyboard
import mouse

#help(mouse)
#help(keyboard)


print('podaj gmine')
gmina = input()

time.sleep(4)

print('ok')



liczenie = 1
while liczenie <= 30:

    time.sleep(0.2)
    keyboard.press_and_release('down')
    
    time.sleep(0.1)
    keyboard.press_and_release('up')

    time.sleep(0.1)
    keyboard.press_and_release('ctrl + alt + r')
    time.sleep(0.1)

    keyboard.wait('shift + -')
    keyboard.write(gmina)
    time.sleep(0.1)
    mouse.wait(button='left')
    #keyboard.wait('enter')


    time.sleep(0.1)
    keyboard.press_and_release('up')
    time.sleep(0.1)


    keyboard.press_and_release('ctrl + s')
    time.sleep(0.1)
    keyboard.press_and_release('enter')
    time.sleep(0.1)
    #keyboard.press_and_release('down')

    time.sleep(0.1)


    
    print('zapisywanie', liczenie)
    liczenie = liczenie + 1

    #DOROBIĆ WARUNEK BREAK
    
    

print('done')

time.sleep(5)
print('bye bye')
