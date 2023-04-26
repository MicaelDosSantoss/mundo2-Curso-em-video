
t = ' TABUADA '
print(f'\n{t:-^20}\n')

c = 0
m = 0

while True:
    pergunta = int(input('Você deseja qual tabuada: '))

    if pergunta > 0:
        while True:     
            if c < 10:
                c += 1
                m = pergunta * c
                print(f'{pergunta} x {c} = {m}')
            else:
                c = 0
                break
    else:
        break

print('Finalizado')