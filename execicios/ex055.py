#Faça um programa que leia o peso de cinco pessoas.
#No final, mostre qual foi o maior e o menor peso lidos.
#MINHA SOLUÇÃO
maiorPeso = 0
menorPeso = 0
for pessoa in range(1,6):
    peso = float(input('Peso da {}ª pessoa: '.format(pessoa)))
    if peso > maiorPeso:
        maiorPeso = peso
    elif peso < menorPeso or menorPeso == 0:
        menorPeso = peso
print('O maior peso lido foi de {:.1f}Kg \nO menor peso lido foi de {:.1f}Kg'.format(maiorPeso, menorPeso))

#SOLUÇÃO DO GUANABARA:
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}Kg'.format(maior))
print('o menor peso lido foi de {}Kg'.format(menor))