
for i in range(1,6):
    peso = float(input('Peso da {} pessoa: '.format(i)))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso e \033[1;35m{maior:.2f}kg \033[m\nÉ o menor peso é \033[1;35m{menor:.2f}kg\033[m')