#Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.
primeiro = int(input('Digite o primeiro termo da PA: '))
razão = int(input('Digite a razão: '))
cont = 1
pa = primeiro
while cont <= 10:
    print(pa, end=' ')
    cont += 1
    pa += razão
print('fim')



