from random import randint
cont = 0
corrente = "=" * 40
text = "PAR OU IMPAR".upper()
print(f'\n {corrente} \n \033[2;33m{text:^20}\033[m \n {corrente} \n')

while True:
  
    pergunta = int(input('Digite um número: '))
    valor = str(input('Par ou impar [P/I]: ')).upper().strip()

    bot = randint(0,10)

    soma = pergunta + bot



    if valor == "P":

        if soma % 2 == 0:
            print(f'\n {corrente}\033\n[1;32m{soma}\033[m, Parabéns você ganhou!\n')
            cont += 1
        else:
            break

    elif valor == "I":

        if soma % 2 != 0:
            print(f'\n {corrente} \033\n[1;32m{soma}\033[m, Parabéns você ganhou!\n')
            cont += 1
        else: 
            break
        
print(f'\n {corrente}Você perdeu, o número foi \033\n[1;32m{soma}\033[m, total de partidas ganhas de \033[1;35m{cont}!\033[m\n')