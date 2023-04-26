listaArmazenar = []
valorTotal = 0 

for i in range(0,4):
    print(f'----- {i + 1}º PESSOA -----')

    n = input("Digite o seu nome: ")
    idade = int(input('Digite a sua idade: '))
    s = input('Digite o seu sexo, M \033[1m(Masculino)\033[m ou F\033[1m(Feminino)\033[m: ')
    print('-'*20,'\n')
    nome = n.capitalize()
    sexo = s.upper()
    listaArmazenar.append([nome, idade, sexo])

    valorTotal += listaArmazenar[i][1]

média = valorTotal / 4

c = 0
f = []

for lista in listaArmazenar:
    
    if listaArmazenar[c][2] == "F" and listaArmazenar[c][1] < 20:
        f += lista
    
    if listaArmazenar[c][2] == "M":
       if c == 0:
         m = lista
       else:
           if lista[1] > m[1]:
               m = lista
    c += 1 


print(f'{m[0]} é o Homem mais velho, ele tem {m[1]}.')

if f == []:
    print('Não existe nenhuma mulher que tenha menos de 20 anos.')
else:
    feminino = f[::3]
    f_str = ', '.join(feminino)
    print(f'As mulheres que tem menos de 20 anos são, {f_str}')

print(f'A média de idade é {média:.0f}')