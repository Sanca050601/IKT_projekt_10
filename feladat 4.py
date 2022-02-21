import random
szam=random.randint(1,5)
gondoltszam=int(input('Mondj egy számot te buzi: '))

if szam==gondoltszam:
    print('TELITALÁLAT')
elif szam<gondoltszam:
    print('A számod nagyobb')
    print(szam)
elif szam>gondoltszam:
    print('A számod kisebb')
    print(szam)