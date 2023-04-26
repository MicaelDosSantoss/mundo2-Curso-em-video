from datetime import date

d = date.today().year

for c in range (0,8):
    s = int(input(f'Digite ano de nascimento: '))

    r = d - s
    
    if r == 18 :
        print(f'Parabens, você está na maior idade {r}')
    elif r > 18:
        print(f'Você ultrapassou a maior idade {r}')
    else:
        print('Você ainda não completou a maior idade')
