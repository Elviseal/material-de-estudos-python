#Faça um programa que calcule a soma entre todos os números que são múltiplos de três
#e que se encontram no intervalo de 1 até 500
soma = 0
cont = 0
for c in range(1, 500, 2):
    if c % 3 == 0:

        soma += c
        cont += 1
print('A soma de todos os {} valores é {} '.format(cont,soma))
#esse exercício foi muito ruím de fazer por qual do enuciado que pedia outra coisa




