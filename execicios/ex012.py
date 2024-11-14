preço = float(input('digite o preço do produto R$'))
desconto = (preço * 5)/100
print('o produto custava R${:.2f}, e na promoção com desconto de 5% custara R${:.2f}'.format(preço,preço-desconto))
#desconto de produto