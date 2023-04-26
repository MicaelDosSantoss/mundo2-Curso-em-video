s = 0
c = 0

for n in range(1, 501, 2):
   if n % 3 == 0:
      c += 1 
      s += n
   
print(f'Quantidade de números somados é de {c}, total de {s}')   