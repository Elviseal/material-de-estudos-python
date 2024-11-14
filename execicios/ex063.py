#Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N
# primeiros elementos de uma Sequência de Fibonacci. Exemplo:
#0 – 1 – 1 – 2 – 3 – 5 – 8
termos = int(input('Quantos termos quer ver:'))
cont = 3
t1 = 0
t2 = 1
print('{} {} '.format(t1, t2), end='')
while cont <= termos:
    t3 = t1 + t2
    print('{} '.format(t3), end='')                     #   t1 t2
    t1 = t2 #esse processo leva as variaveis para direita 0  1  2  3
    t2 = t3
    cont += 1
print('fim')

