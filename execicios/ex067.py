#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
#O programa será interrompido quando o número solicitado for negativo.
mult = 0
while True:
    tabuada = int(input('Qual tabuada deseja ver: '))
    if tabuada < 0:
        print('Programa encerrado! Volte sempre!')
        break
    print('-' * 30)
    if tabuada > 0:
        cont = 0
        while cont < 10:
            cont += 1
            mult = tabuada * cont
            print(f'{tabuada}x{cont}={mult}')
    print(30 * '-')

