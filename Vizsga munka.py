print('1. feladat')
x = (input('Jó napod van zsigo? '))

if(x=='Igen'):
    print('Az fasza')
elif(x=='Nem'):
    print('Az szar, depizz')
else:
    print('Sajnos hülye vagy!')

print('2. feladat')
x= int(input('Mondj már egy számot!!! '))
if(x%2):
    print('Páratlan szám')
elif(x!=0):
    print('Páros szám')
else:
    print('A szám 0')

print('3. feladat')

import random

y = random.randint(1,5)
s = int(input('Bassz be egy számot: '))

if(s<y):
    print('A számod kisebb, mint a gép által gondolt szám!')
elif(s>y):
    print('A számod nagyobb, mint a gép által gondolt szám!')
else:
    print('A számod egyenlő a gép által gondolt számmal!')