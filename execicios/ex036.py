n = 5 * '--==--'
m = 14 *'--==--'
cores = {'roxo':'\033[4;35m',
'limpa' :'\033[m'}
print('\033[4;35m' '{} Simulador de Emprestimo {}''\033[m'.format(n,n))
#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#Pergunte o valor da casa,
valorCasa = float(input('Qual o valor da casa que deseja financiar? '))
# o salário do comprador
valorSalario = float(input('Qual o salário do comprador? '))
# e em quantos anos ele vai pagar.
prazo = int(input('Qual o prazo de financiamento? '))
prazo = prazo * 12
prestaçao = valorCasa / prazo
#A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
limiteSalario = valorSalario * 30/100
if prestaçao >= limiteSalario:
    print('Para o finaciamento de R${:.2f}, a prestação fica {:.2f}, com sua renda de R${:.2f}'.format(valorCasa,prestaçao,valorSalario))
    print('Financiamento negado!')
else:
    print('Para o finaciamento de R${:.2f}, a prestação fica {:.2f}, com sua renda de R${:.2f}'.format(valorCasa, prestaçao, valorSalario))
    print('Financiament cocedido!')


print('{}{}{}'.format(cores['roxo'], m, cores['limpa']))
