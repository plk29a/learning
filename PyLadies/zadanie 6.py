#TREŚĆ ZADANIA

#Napisz funkcję, która jako argument przyjmie dowolny tekst i zwróci słownik, którego
#kluczami będą wszystkie słowa z tego tekstu, a wartościami będą liczby wystąpień tych
#słów w tekście. Funkcja powinna być obojętna na wielkość liter (czyli 'Kot' i 'kot' mają być
#traktowane jako jedno słowo) i powinna ignorować znaki interpunkcyjne.

#>>> tekst = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer sollicitudin ultricies eros, vitae eleifend ipsum sodales ut. Pellentesque libero ipsum, euismod eget volutpat nec, hendrerit vel turpis."
#>>> licz_slowa(tekst)
#{'sollicitudin': 1, 'elit': 1, 'vel': 1, 'eleifend': 1, 'sodales': 1, 'eros': 1, 'sit': 1, 'nec': 1, 'consectetur': 1, 'pellentesque': 1, 'vitae': 1, 'eget': 1, 'hendrerit': 1, 'dolor': 1, 'turpis': 1, 'euismod': 1, 'integer': 1, 'lorem': 1, 'amet': 1, 'ipsum': 3, 'ut': 1, 'ultricies': 1, 'libero': 1, 'adipiscing': 1, 'volutpat': 1}

print('Liczenie słów')
tekst = 'Ala ma kota. Kota nie ma Krzyś.'

def licz_slowa(tekst):
    slownik_slow={} #wiek = {'Marcin': 23, 'Agata': 17, 'Marta': 46}
