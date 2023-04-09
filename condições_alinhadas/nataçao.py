from datetime import date

d = date.today().year

r = int(input('digite o seu ano de nascimento: '))

idade = d - r

print(f'{idade} anos.')

if idade >= 9 and idade < 14:
    print('Você é da natação\033[4;35m MIRIM\033[m.')
    
elif idade >= 14 and idade < 19:
    print('Você é da natação\033[4;35m INFANTIL\033[m.')

elif idade >= 19 and idade < 25:
    print('Você é da natação\033[4;35m JUNIOR\033[m.')

elif idade == 25:
    print('Você é da natação\033[4;35m SÊNIOR\033[m.')
else:
    print('Você é da natação\033[4;35m MASTER\033[m.')