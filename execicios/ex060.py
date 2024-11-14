#Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
#5! = 5 x 4 x 3 x 2 x 1 = 120
#FEITO IMPORTANDO CLASSE E METODOS
from math import factorial
n = int(input('Digite o número para fatorial: '))
f = factorial(n)
print('{}'.format(f))
#FEITO COM LAÇO FOR
nu = int(input('Qual número deseja o fatorioal: '))
fat = 1
print('{}!='.format(nu),end='')
for nu in range(nu, 0, -1):
    fat *= nu
    print('{}'.format(nu), end='')
    print('x'if nu > 1 else '=', end='')
print('{}'.format(fat))
#FEITO COM LAÇO WHILE
n1 = int(input('Qual o número: '))
c = n1 + 1
fato = 1
print('{}!='.format(n1), end='')
while c > 1:
    c -= 1
    fato *= c
    print('{}'.format(c),end='')
    print('x'if c > 1 else '=', end='')
print('{}'.format(fato))
