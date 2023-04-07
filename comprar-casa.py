casa = float(input('Qual o valor da casa: '))
salario = float(input('Qual o seu salário mensal: '))
anos = int(input('Em quandos anos será pago: '))

trinta = salario * 30 / 100

d = casa / (anos * 12)

if d <= trinta:
    print(f'Você poderá comprar a casa:  Salário 30%:\033[4;34m R$ {trinta:.2f},\033[m\nValor mensal da casa \033[4;35m R$ {d:.2f} \033[m.')
else: 
    print(f'Você não poderá comprar a casa, salario mensal R$ {trinta:.2f}, valor da casa mensal R$ {d:.2f}.')
