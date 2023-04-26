c = str(input('Digite o seu sexo: ')).strip().upper()

while c not in 'MF':

  
  c =input('Sexo invalido, digite novamente: ').strip().upper()
print('Sexo valido!')