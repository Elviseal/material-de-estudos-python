#Crie um programa que leia vários números inteiros pelo teclado.
#No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
#O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
soma = cont = maior = menor = 0
conti = 'S'
while conti in 'Ss':
    núm = int(input('Digite um número: '))
    soma += núm
    cont += 1
    if cont == 1:
        maior = menor = núm
    else:
        if núm > maior:
            maior = núm
        if núm < menor:
            menor = núm
    conti = str((input('Quer continuar [S/N]'))).strip().upper()[0]
media = soma / cont
print('Você digitou tantos números {} e a média é {:.1f}, o maior número foi {} e o menor foi {}'.format(cont, media, maior, menor))