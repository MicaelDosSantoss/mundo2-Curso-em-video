n = int(input('Primeiro termo: '))
r = int(input('Razão de PA: '))
t = n
c = 1
total = 0
m = 10

while m != 0:
    total = total + m
    while c <= total:
        print(f'{t} => ', end='')
        t += r
        c += 1
    print('Pausa!')
    m = int(input('Você deseja mais ?: '))
print('FIM')