n1 = int(input('digite o primeiro número: '))
n2 = int(input('digite o Segundo número: '))

v = True

while v == True:

    menu = int(input('[1] Somar\n[2] Multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa\nQual opção você deseja: '))

    if menu == 1:
        total = n1 + n2
        print(f'\nA soma entre {n1} + {n2} é {total}\n')
    if menu == 2:
        total =  n1 - n2
        print(f'\nA multiplicação entre {n1} - {n2} é {total}\n')
    if menu == 3:
       if n1 > n2:
           print(f'\nO maior número é {n1}\n')
       else: 
           print(f'\nO maior número é {n2}\n')
    if menu == 4:
        n1 = int(input('digite o primeiro número: '))
        n2 = int(input('digite o Segundo número: '))
    if menu == 5:
        v = False
    else:
        v = False
        print('\nDado invalido, tente novamente! ')
print('\nFim do procedimento! \n')