#Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep
opção = 0

nu1 = int(input('Primeiro número: '))
nu2 = int(input('Segundo número: '))
while opção != 5:
    print('''[1] SOMAR
[2]MULTIPLICAÇÃO
[3]MAIOR
[4]NOVOS NÚMEROS
[5]SAIR DO PROGRAMA''')
    opção = int(input('>>>>> Qual a sua opção? '))
    if opção == 1:
        soma = nu1 + nu2
        print('A somar entre {} + {} é {}'.format(nu1, nu2, soma))
    elif opção == 2:
        mult = nu1 * nu2
        print('A multiplicação entre {} x {} é {}'.format(nu1,nu2,mult))
    elif opção == 3:
        if nu1 > nu2:
            maior = nu1
        else:
            maior = nu2
            print('O número maoir entre {} e {} é {}'.format(nu1,nu2,maior))
    elif opção == 4:
        print('Iforme os números novamente:')
        nu1 = int(input('Primeiro número: '))
        nu2 = int(input('Segundo número: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida.Tente novamente')
    print('=-='*10)
    sleep(2)
print('Fim do programa! Volte sempre!')









