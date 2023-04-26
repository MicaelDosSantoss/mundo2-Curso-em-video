pergunta = str(input('Digite o frase: '))

s = pergunta.upper()
t = ''.join(s.split())
i = '' # armazenador da frase invertida

for c in range(len(t) -1, -1, -1):
    i += t[c] # Esse laço de repetição inverte as letras

if t == i:
    print(f'{t} virou {i}, é um palíndromo')
else:
    print(f'{t} virou {i}, não é um palíndromo')