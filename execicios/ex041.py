#A Confederação Nacional de Natação precisa de um programa
# que leia o ano de nascimento de um atleta e mostre sua categoria,
# de acordo com a idade:
from datetime import date
dataAtual = date.today().year
nascimento = int(input('Digite o ano de nascimento do atleta: '))
idade = dataAtual - nascimento
print('Com {} anos o atleta faz parte da categoria: '.format(idade))
#– Até 9 anos: MIRIM
if idade <= 9:
    print('MIRIM')
#– Até 14 anos: INFANTIL
elif idade <= 14:
    print('INFANTIL')
#– Até 19 anos: JÚNIOR
elif idade <= 19:
    print('JÚNIOR')
#– Até 25 anos: SÊNIOR
elif idade <= 25:
    print('SÊNIOR')
#– Acima de 25 anos: MASTER
else:
    print('MASTER')
