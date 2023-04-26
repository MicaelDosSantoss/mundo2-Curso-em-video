
n = 0
c = 0

while True:
    pergunta = int(input('Digite um número (999 para parar): '))
    

    if pergunta == 999:
        break
    c += 1
    n += pergunta

print(f'O total de vezes digitadas foi de {c}, número total foi {n}.')