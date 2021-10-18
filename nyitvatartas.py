time = (input('Hány óra van most? '))
time = int(time)
if(time>=8 and time<=16):
    print('A bolt nyitva van')
    print('Még ennyi órád van vásárolni: ', 32-time)
else:
    print('A bolt zárva van')
    print('Ennyi óra múlva lesz nyitva: ', 8-time)
