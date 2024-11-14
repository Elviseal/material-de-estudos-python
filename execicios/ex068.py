# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
cont = 0
while True:
    print('{:-^60}'.format('JOGO PAR OU ÍMPAR'))
    jogador = int(input('Escolha um número: '))
    compu = randint(0, 10)
    soma = jogador + compu
    parimpar = ' ' # começei essa variavel vazia para fazer o teste
    while parimpar not in 'PI': #teste
        parimpar = str(input('PAR OU IMPAR [P/I] ')).upper().strip()[0]
    print(f'Você digitou {jogador} e o computador {compu} .Total {soma}', end=' ' )
    print('É PAR' if soma % 2 == 0 else 'É ÍMPAR')
    if parimpar == 'P':
        if soma % 2 == 0:
            print('VOCÊ VENCEU!')
            cont += 1
        else:
            print('VOCÊ PERDEU!')
            break
    elif parimpar == 'I':
        if soma % 2 == 1:
            print('VOCÊ VENCEU!')
            cont += 1
        else:
            print('VOCÊ PERDEU!')
            break
print(f'Números de vitórioas {cont}')
print(30 * '-')
