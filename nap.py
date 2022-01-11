while True:

    val = input('Melyik nap? ')
    
    try:
        if val=='Hétfő':
            print('1. nap hétköznap') 
            break
        if val=='Kedd':
            print('2. nap hétköznap') 
            break
        if val=='Szerda':
            print('3. nap hétköznap') 
            break
        if val=='Csütörtök':
            print('4. nap hétköznap') 
            break
        if val=='Péntek':
            print('5. nap hétköznap') 
            break
        if val=='Szombat':
            print('6. nap hétvége') 
            break
        if val=='Vasárnap':
            print('7. nap hétvége') 
            break
        else:
            print('Nem jól írod te fasz! ', end="")

    except Exception:
        print('Error')
