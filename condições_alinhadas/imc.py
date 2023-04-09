peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura\033[1m (Em metros) \033[m: '))

imc = peso / (altura ** 2)
print(f'IMC {imc}')

if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 <= imc < 25:
    print('Peso ideal')
elif 25 <= imc < 30:
    print('Sobre peso')
elif 30 <= imc < 40:
    print('Obesidade')
else:
    print('Obesidade Mórbida')

