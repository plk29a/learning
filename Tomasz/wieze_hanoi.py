def hanoi(n, A, B, C):
    if n > 0:
        hanoi(n-1, A, C, B)
        print(f'przenieś krążek z wieży {A} do wieży {C}')

        hanoi(n-1, B, A, C)


hanoi(4, 'a', 'b', 'c')


d = [1, 2, 3, 4]
e = []
f = []

def hanoi(n, A, B, C):
    if n > 0:
        hanoi(n-1, A, C, B)
        C.insert(0, A.pop(0))
        print(f'wieża A: {A}, wieża B: {B}, wieża C: {C}')
        hanoi(n-1, B, A, C)

hanoi(4, d, e ,f)
print(d, e, f)
