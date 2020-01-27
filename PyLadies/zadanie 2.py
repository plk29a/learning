print('zadanie 2')

listaslownikow = [{'znak' : '1', 'co to?' : 'cyfra'},
     {'znak' : 'a', 'co to?' : 'litera'},
     {'znak' : '2', 'co to?' : 'cyfra'},
     {'znak' : 'b', 'co to?' : 'litera'},
     {'znak' : '3', 'co to?' : 'cyfra'},
     {'znak' : '4', 'co to?' : 'cyfra'},
     {'znak' : 'c', 'co to?' : 'litera'},
     {'znak' : 'd', 'co to?' : 'litera'},
     {'znak' : '!', 'co to?' : 'inny'},
     {'znak' : '!', 'co to?' : 'inny'}]

def grupuj(lista, klucz):
    kopia = lista
    pierwszy = lista[0]
    a0 = [lista[0][klucz]]

# policzenie ile jest różnych kluczy i ich wymienienie
    for x in lista:
        if x[klucz] not in a0:
            dodatek = [x[klucz]]
            a0 = a0 + dodatek
            print(a0)
    #print(a0, 'lista wszystkich argumentów', len(a0))

#grupuje po kluczu odpowiednie słowniki + oraz tworzy ich listę.
    petla = 0
    while petla < len(a0):
        slownik = []
        b = a0[petla]
        for x in lista:
            if x[klucz] == b:    
                #print(x)
                slownik.append(x)
        print(b, slownik)
        petla = petla + 1
    #return b, slownik            - czy to wogóle potrzebne
        

grupuj(listaslownikow, 'co to?')


