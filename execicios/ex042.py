#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
from time import sleep #importa a classe e o metodo
reta1 = int(input('Digite a primeira reta: '))
reta2 = int(input('Digite a segunda reta: '))
reta3 = int(input('Digite a teceira reta: '))
print('Calculando o tamanho das retas...')
sleep(1) #faz o computador esperar
print('primeira {}, segunda {} e teceira {}'.format(reta1, reta2, reta3))
if reta1 + reta2 > reta3 and reta2 + reta3 > reta1 and reta3 + reta1 > reta2:
    print('Essas retas podem formar um triângulo')
#– EQUILÁTERO: todos os lados iguais
    if reta1 == reta2 and reta1 == reta3:
        print('Triângulo EQUILÁTERO todos os lados iguais')
#– ISÓSCELES: dois lados iguais, um diferente
    elif reta1 == reta2 != reta3 or reta1 == reta3 != reta2:
        print('triângulo ISÓSCELES: dois lados iguais ')
#– ESCALENO: todos os lados diferentes
    else:
        print('triângulo ESCALENO: todos os lados diferentes')
else:
    print('Essas retas não podem formar um triângulo')