p = int(input('Digite um número: '))
r = int(input('Você deseja \033[1;35m [1] BINARIO\033[m, \033[1;34m [2] OCTAL\033[m, \033[1;32m [3] HEXADECIMAL\033[m : '))

if 1 == r:
    t = bin(p)
    print(f'  \033[1;35m BINARIO : {t}\033[m')
elif 2 == r:
    t = oct(p)
    print(f'\033[1;34m OCTAL : {t}\033[m')
elif 3 == r:
    t = hex(p)
    print(f'  \033[1;35m HEXADECIMAL : {t}\033[m')
else:
    print('Resultado não encontrado!')