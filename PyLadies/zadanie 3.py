print('delta_compression')
lista = [5, 7, 11, 21, 28, 6, 7]


def delta_compression(lista):
#sortowanie listy
    lista = sorted(lista)
#wypisywanie delty
    lista_wynikowa = [lista[0]]
    poprzednia = lista[0]
    for nastepna in lista:
        roznica = nastepna - poprzednia
        poprzednia = nastepna
        lista_wynikowa.append(roznica)
    lista_wynikowa.remove(0)
    return(lista_wynikowa)
print('orginalna lista:     ', lista)
print('działanie definicji:', delta_compression(lista))
