#Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.
from random import randint
computador = randint(0,10)
acertou = False #criou essa variavél para fazer o no começo do laço
tentativas = 0
print('Sou seu computador...\nAcabei de pensar em um múmero entre 0 e 10\nSerá que você consegue advinhar qual foi?')
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    tentativas += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('O número é maior')
        elif jogador > computador:
            print('O número é menor')
print('Acetou em {} tentativas. parabéns!'.format(tentativas))
