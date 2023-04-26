
corrente = '=-=' * 20
total = 0
produtosMais = 0

RecebeProduto = ''
RecebeDinheiro = 0

print(f'{corrente}\n \033[1mLOJÃO\033[m\n{corrente}\n')

produto = str(input('\nNome do produto: ')).capitalize()
din = float(input('Qual o preço R$'))

RecebeDinheiro = din
RecebeProduto = produto

while True:
  

    if din < RecebeDinheiro:
        RecebeDinheiro = din
        RecebeProduto = produto


    total += din

    if din > 1000:
        produtosMais += 1

    g = str(input('\nDeseja adicionar mais [S/N]: ')).strip().upper()

    if g == 'N':
        break
    
    produto = str(input('\nNome do produto: ')).capitalize()
    din = float(input('Qual o preço R$'))

print(f'Total da compra e de \033[1;32mR${total:.2f}\033[m, Existem \033[1;35m{produtosMais}\033[m que estão acima de R$1.000,00.\nO produto mais barato e o \033[1;35m{RecebeProduto}\033[m que custa \033[1;32mR${RecebeDinheiro:.2f}\033[m\n')
    