# -*- coding: cp1250 -*-

import time
import keyboard.keyboard as keyboard #pierwszy zapis z kropk� wskazuje �cie�k�, as inaczej nazywa modu�.
#from tkinter import Label, Entry, Button - taki zapis mo�e pobra� tylko niekt�re funkcje z ca�ej biblioteki.


#help(mouse)
#help(keyboard)

print('ile rekordow?')

nr_rekord = input()
nr_rekord = int(nr_rekord)

print('Zapisz pierwszy plik jako kml w dobrej scia�ce')
print('Enter uruchamia dalszy proces')

keyboard.wait('enter')

time.sleep(1)
print(3)
time.sleep(1)
print(2)
time.sleep(1)
print(1)
time.sleep(1)
print('go')

keyboard.press_and_release('down')

for i in range(1, nr_rekord): #funkcja for nie wymaga czego� do liczenia :)

    time.sleep(0.3)
    keyboard.press_and_release('ctrl + s')
    time.sleep(0.2)
    keyboard.press_and_release('enter')
    time.sleep(0.3)
    keyboard.press_and_release('down')

    print('zapisywanie', i + 1)


print('done')
time.sleep(5)
