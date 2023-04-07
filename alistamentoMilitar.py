from datetime import date

r = int(input('Ano de nascimento: '))

d = date.today().year
t = d - r

if t == 18:
    print(f'Você precisa se alistar esse ano de \033[1;35m{d}\033[m.')
elif t > 18:
    f = t - 18
    print(f'Você já deveria ter ser alistado a \033[1;32m{f} anos.\033[m.')
else:
    f = 18 - t
    print(f'Ainda falta \033[1;33m{f} anos\033[m para o alistamento.')
