
n = int(input('Quantos termos você deseja: '))
c = 3

t = 0
r = 1

print(f'{t} => {r}', end='')

while c <= n:
    t1 = t + r
    print(f' => {t1} ', end='')
    t = r
    r = t1
    c += 1
print('fim')