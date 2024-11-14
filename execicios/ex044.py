#Elabore um programa que calcule o valor a ser pago por um produto,
#considerando o seu preço normal e condição de pagamento:,
print('\033[40;31m {:=^60} \033[m'.format('LOJA DO ELVIS')) #centraliza oque esta no format
valorProduto = float(input('Valor do Produto: R$ '))
print('\033[31m', '''Formas de Pagamento:
 [1] DINHERIO/CHEQUE
 [2] VISTA NO CARTÃO 
 [3] 2X CARTÃO 
 [4] 3X CARTÃO ou mais ''', '\033[m')
formaDePagamento = str(input('Selecione: ')).upper().strip()
print('Valor do produto sem desconto R$ {}'.format(valorProduto))
#– à vista dinheiro/cheque: 10% de desconto
if formaDePagamento == '1':
    novoValor = valorProduto - (10 * valorProduto / 100)
    print('Valor com desconto de 10% R${}'.format(novoValor))

#– à vista no cartão: 5% de desconto
elif formaDePagamento == '2':
    novoValor = valorProduto - (5 * valorProduto / 100 )
    print('Valor com desconto de 5% R${}'.format(novoValor))

#– em até 2x no cartão: preço formal
elif formaDePagamento == '3':
    novoValor = valorProduto / 2
    print('Em duas vezes de R$ {}, sem juros'.format(novoValor))

#– 3x ou mais no cartão: 20% de juros
elif formaDePagamento == '4':
    novoValor = valorProduto + (20 * valorProduto / 100)
    parcelas = int(input('Digite a quantidade de parcelas: '))
    total = novoValor / parcelas
    print('Produto parcelado em {}x vai ficar R${:.2f} com juros e a parcela é de R$ {:.2f}'.format(parcelas,novoValor,total))
else:
    print('Opção Invalida!')