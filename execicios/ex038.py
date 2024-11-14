#Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
nu1 = int(input('Digite o primeiro número: '))
nu2 = int(input('Digite o segundo número: '))
# O primeiro valor é maior
if nu1 > nu2:
    print('O número {} é o primeiro e o maior '.format(nu1))
# O segundo valor é maior
elif nu2 > nu1:
    print('O número {} é o segundo e é maior'.format(nu2))
# Não existe valor maior, os dois são iguais
elif nu1 == nu2:
    print('Não existe valor maior, os dois são iguais')
