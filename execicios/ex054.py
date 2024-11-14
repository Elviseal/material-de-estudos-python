#Crie um programa que leia o ano de nascimento de sete pessoas. No final,
# mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
dataAtul = date.today().year
cont = 0
resto= 0
for pessoas in range(1,8):
    anoNasc = int(input('Em que ano {}ªvocê nasceu: '.format(pessoas)))
    idade = dataAtul - anoNasc
    if idade >= 21:
        cont += 1
    else:
        resto = pessoas - cont
print('Ao todo tivemos {} pessoas maiores de idade'.format(cont))
print('E também tivemos {} pessoas menores de idade'.format(resto))


