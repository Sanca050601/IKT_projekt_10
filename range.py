print('1. feladat')

a = int(input('Szám_1: '))
b = int(input('Szám_2: '))
c = int(input('Szám_3: '))
x = min(a, b, c)
print('A legkisebb:', x)

a = int(input('Szám_1: '))
b = int(input('Szám_2: '))
c = int(input('Szám_3: '))
y = max(a, b, c)
print('A legnagyobb:', y)

x = int(input('A pontszámod: '))
if(0<=x<25):
    print('EGYES, MEGBUKTÁL')
if(25<=x<50):
    print('KETTES, ÁTMENTÉL')
if(50<=x<75):
    print('HÁRMAS')
if(75<=x<90):
    print('NÉGYES')
if(90<=x<=100):
    print('ÖTÖS, SZÉP MUNKA')
else:
    print('Nem értékelhető szám')