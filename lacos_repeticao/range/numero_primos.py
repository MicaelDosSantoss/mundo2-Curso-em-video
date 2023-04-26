p = int(input('Digite um número: '))

for c in range(1,p + 1):
    if p % c == 0:
        print(f'\033[32m', end=' ')
    else:
        print('\033[31m', end=' ')
    print(f'{c}',end='')