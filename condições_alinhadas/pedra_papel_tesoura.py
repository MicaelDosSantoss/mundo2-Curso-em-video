from random import randint
import emoji

corrente = ('=-=' * 10)
print(f'{corrente} PEDRA, PAPEL, TESOURA {corrente}')

ped = emoji.emojize(':oncoming_fist:', language='alias')
pap = emoji.emojize(':raised_back_of_hand:', language='alias')
tes = emoji.emojize(':victory_hand:', language='alias')

pergunta = int(input('[1] Pedra\n[2] Papel\n[3] Tesoura\nEscolha um: '))

# Programa aleatorio

bot = randint(1,3)

# jogo

if pergunta == bot:
    print(f'Empate!')
else:
    # Pedra x tesoura
    if pergunta == 1 and bot == 3:
        print(f'\nPEDRA{ped} x {tes}TESOURA\nJogador, Venceu!')

    elif bot == 1 and pergunta == 3:
        print(f'\nTESOURA{tes} x {ped}PEDRA\nBot, Venceu!')

    # Papel x pedra
    elif pergunta == 2 and bot == 1:
        print(f'\nPAPEL{pap} x {ped}PEDRA\nJogador, Venceu!')
    
    elif bot == 2 and pergunta == 1:
        print(f'\nPEDRA{ped} x {pap}PAPEL\nBot, Venceu!')
    
    # Tesoura x papel

    elif pergunta == 3 and bot == 2:
        print(f'\nTESOURA{tes} x {pap}PAPEL\nJogador, Venceu!')
    
    elif bot == 3 and pergunta == 2:
        print(f'\nPAPEL{pap} x {tes}TESOURA\nBot, Venceu!')   

    # Tesoura x Pedra

    elif pergunta == 1 and bot == 3:
        print(f'\nPEDRA{ped} x {tes}TESOURA\nJogador, Venceu!')
    
    elif bot == 3 and pergunta == 1:
        print(f'\nTESOURA{tes} x {ped}PEDRA\nBot, Venceu!')  
    else:
        print('resultado não encontrado!')   