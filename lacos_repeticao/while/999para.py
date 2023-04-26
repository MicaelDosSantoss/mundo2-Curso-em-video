
n1 = int(input('Digite um número [999 para parar]: '))
cont = 0
v = True
c = 0

while n1 != 999:
    c += n1    
    cont += 1
    n1 = int(input('Digite um número [999 para parar]: '))
      
print(f'Quantidada total de {c}, é quantidade digitada é de {cont}')
