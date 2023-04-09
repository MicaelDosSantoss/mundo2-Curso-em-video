pag = float(input('preço da compra: R$'))

form = int(input('Forma de pagamento\n[1] à vista dinheiro/cheque\n[2] à vista no cartão\n[3] 2x no cartão\n[4] 3x no cartão\nQual é a opção: '))

if form == 1:
    total =  pag - (pag * 10 / 100) 

elif form == 2:
    total = pag - (pag * 5/100)

elif form == 3:
    total = pag
    par = pag / 2
    print(f'2x de R${total:.2f} igual à R${par:.2f}')

elif form == 4:
    total = pag + (pag * 20 / 100)
    quanPar = int(input('Quantas parcelas você deseja: '))
    par = total / quanPar
    print(f'compra parcela em {quanPar:.2f}x de R${pag:.2f}, parcela de R${par:.2f} por mês')
else:
    total= 0
    print('Opção invalida, tente novamente!')

print(f'Total do pagamento R${total:.2f}')