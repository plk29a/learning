print('cięcie stringa')
a = '12'
b = '12345'
c = '123456'
d = '12345678910111213141516'
e = 'abcdefg'


def tnij (string, dl):

    if len(string) < dl:
        global lista
        lista = [string]
        
        if len(string) == 0: #tego da się napewno jaość uniknąć w kodzie, ale nie wiem jak :(, ma za zadanie usunąć pustego stringa z końca listy.
            lista.pop()
            
    else:
        tnij(string[dl:], dl)
        lista.insert(0, string[:dl])
        
    return lista


print(tnij(d,5))

print(tnij(a,1))
