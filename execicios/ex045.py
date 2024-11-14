#Crie um programa que faça o computador jogar Jokenpô com você.
import random
from time import sleep

print('''SUAS OPÇÕES: 
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
opção = int(input('Escolha é sua jogada? '))
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
lista = [0,1,2]
jogo = random.choice(lista) #embaralha a lista
print(5*'-=-=-')
if jogo == 0:
    print('Computador jogou PEDRA')
    if opção == 0:
        print('Jogador jogou PEDRA')
        print(5 * '-=-=-')
        print('EMPATE!')
    elif opção == 1:
        print('jogador jogou PAPEL')
        print(5 * '-=-=-')
        print('JOGADOR VENCEU!')
    elif opção == 2:
        print('Jogador jogou TESOURA')
        print(5 * '-=-=-')
        print('COMPUTADOR VENCEU!')
elif jogo == 1:
    print('Computador jogou PEDRA')
    if opção == 0:
        print('Jogador jogou PEDRA')
        print(5 * '-=-=-')
        print('EMPATE!')
    elif opção == 1:
        print('jogador jogou PAPEL')
        print(5 * '-=-=-')
        print('JOGADOR VENCEU!')
    elif opção == 2:
        print('Jogador jogou TESOURA')
        print(5 * '-=-=-')
        print('COMPUTADOR VENCEU!')
elif jogo == 2:
    print('Computador jogou PEDRA')
    if opção == 0:
        print('Jogador jogou PEDRA')
        print(5 * '-=-=-')
        print('EMPATE!')
    elif opção == 1:
        print('jogador jogou PAPEL')
        print(5 * '-=-=-')
        print('JOGADOR VENCEU!')
    elif opção == 2:
        print('Jogador jogou TESOURA')
        print(5 * '-=-=-')
        print('COMPUTADOR VENCEU!')








