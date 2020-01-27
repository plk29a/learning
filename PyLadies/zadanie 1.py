print('Funkcja title')

x = 'aLa Ma, kOTA'

def title2 (x):
    
    x = x.lower()
    y = ''

    for slowo in x.split():
        slowo = slowo.replace(slowo[0],  slowo[0].upper(), 1)
        z = y + slowo + ' ' 
        y = z
        z = z.strip()

# ewentualne uwzględnianie jednej spacji na krańcach.
    if x[0] == ' ' and x[-1] == ' ':
        z = ' ' + z + ' '
    elif x[0] == ' ':
        z = ' ' + z
    elif x[-1] == ' ':
        z = z + ' '
    else:
        z = z.strip()

#program nie ogarnia "," itp. to znaczy a,a zamieni jako A,a - powinno być A,A        
    return(z)

#opinia
print(x, '- orgianlny tekst')
print(title2(x), '- działanie funkcji')
if title2(x) == x.title():
    print('Zaliczone')
else:
    print('do poprawy')

