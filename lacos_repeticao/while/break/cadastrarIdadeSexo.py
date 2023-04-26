Idade = 0
Masculino = 0
Mulheres_com_menos_de_vinte_anos = 0

print('{}\n \033[1;33mCADASTRO PESSOAL\033[m\n {}'.format('='*40,'='*40))

while True:
    i = int(input('\nDigite a sua idade: '))
    s = str(input('Digite o seu sexo [M/F] : ')).upper()

    if i > 18:
        Idade += 1
    if s == 'M':
        Masculino += 1
    if s == 'F' and i < 20:
        Mulheres_com_menos_de_vinte_anos += 1
    
    pergunta = ' '

    while pergunta not in 'SN':
        pergunta = str(input('\nDeseja continuar [S/N] : ')).upper().strip()

    if pergunta == "N":
        break


print(f'\nHá \033[1;35m{Idade}\033[m que tem menos de 18 anos.\nQuantidade de homens é \033[1;35m{Masculino}\033[m.\nMulheres com menos de 20 anos \033[1;35m{Mulheres_com_menos_de_vinte_anos}\033[m\n')