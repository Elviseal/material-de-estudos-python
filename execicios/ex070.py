#Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.

# B) quantos produtos custam mais de R$1000.

# C) qual é o nome do produto mais barato.
total = maismil = menorpreço = cont = 0
nomem = ''
while True:
    nome = str(input('Nome do produto: '))
    preço = float(input('Preço: R$ '))
    cont += 1
    if cont == 1 or preço < menorpreço:
        menorpreço = preço
        nomem = nome
    if preço > 1000:
        maismil += 1
    total += preço

    conti = ' '
    while conti not in 'SN':
        conti = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if conti == 'N':
        break

print(f'Tatal da comprar:R${total:.2f}')
print(f'Produtos com o valor maior que mil reais {maismil}')
print(f'Produto mais barato {nomem} R$ {menorpreço}')
print('{:-^40}'.format(' FIM DO PROGRAMA '))