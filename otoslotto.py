import random
lotto_szamok=[random.randint (1,90) for faszom in range(5)]
lotto_szamok.sort()
print(f'A kisorsolt számok: {str(lotto_szamok)[1:-1]}')

