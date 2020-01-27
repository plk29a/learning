print('grupuj i licz')
import datetime
krotka = [(datetime.date(2015, 3, 17), 10), (datetime.date(2015, 3, 30), 12), (datetime.date(2015, 4, 14), 11), (datetime.date(2015, 4, 28), 10), (datetime.date(2015, 5, 1), 9), (datetime.date(2015, 5, 2), 9), (datetime.date(2016, 2, 2), 9), (datetime.date(2016, 2, 4), 3), (datetime.date(2017, 2, 7), 666)]



def grupuj_i_licz(krotka):
    sorted(krotka)
    miesiac = krotka[0][0].month
    suma = 0
    x = 0
    slownik = {}
    datownik = krotka[0][0].month
    datownikrok = krotka[0][0].year
    
    for data in krotka:
        
        if data[0].month == datownik and datownikrok == data[0].year: 
            suma = suma + data[1]

        else:
            slownik[datownikrok, datownik] = suma
            suma=data[1]
        datownik = data[0].month
        datownikrok = data[0].year

    
    slownik[datownikrok, datownik] = suma
    print(slownik)


print ('działanie programu')
grupuj_i_licz(krotka)    


print('orginalna lista krotek:')
print(krotka)
