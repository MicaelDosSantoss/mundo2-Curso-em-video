import random

n1 = int(input('Digite um número de 0 a 10: '))
p = 0
bot = random.randint(1,10)

while n1 != bot:
    n1 = int(input('Você errou, digite novamente: '))
    p += 1
print(f'Você acertou era o {n1}, Parabéns, quantidade de tentativas {p}')