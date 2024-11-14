#conveção de moeda com variavel
reais = float(input('quantos reais você tem em sua carteira: R$'))
dola= reais/3.27
print('com R${:.2f} você consegue compra US${:.2f}'.format(reais,dola))
#sem variavel
print('com R${:.2f} você consegue compra US${:.2f}'.format(reais,reais/3.27))