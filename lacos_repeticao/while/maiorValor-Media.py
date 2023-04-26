per = int(input('Digite um número: '))
v = True
n = 0
c = 1
maior = menor = per

while v == True:
    n += per
    g = str(input('Quer continuar [S/N]: ')).upper().strip()

    if per > maior:
       maior = per
    if per < menor:
       menor = per
    if g == 'S':
     per = int(input('Digite um número: '))
     c += 1
    else:
       v = False

m = n / c

print(f'\033[1;35mMaior:\033[m {maior}, \033[1;35mMenor:\033[m: {menor}, \033[1;35mMédia:\033[m {m}.')
