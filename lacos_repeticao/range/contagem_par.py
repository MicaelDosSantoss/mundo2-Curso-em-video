s = 0

for i in range(0,6):
   c = int(input('Digite os valores: '))
   s += c

if s % 2 == 0:
   print(f'Valor total de {s}')
else:
   print('valor não valido')