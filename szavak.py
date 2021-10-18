szo1 = input('Első szó: ')
szo2 = input('Második szó: ')

szo1 = len(szo1)
szo2 = len(szo2)

if szo1 > szo2:
    print('A hosszabb szó:', szo1)
elif szo2 > szo1:
    print('A hosszabb szó:', szo2)
else:
    print('A két szó egyforma hosszú')