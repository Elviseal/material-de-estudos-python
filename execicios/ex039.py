from datetime import date
#Faça um programa que leia o ano de nascimento de um jovem e informe,
sexo = str(input('Digite M para MASCULINO  e F para FEMININO: ')).upper().strip()
if sexo == 'M':
    nascimento = int(input('Digite o ano de nascimento: '))
    dataAtul = date.today().year
#de acordo com a sua idade,
    idade = dataAtul - nascimento
#se ele ainda vai se alistar ao serviço militar,
    if idade < 18:
        saldo = 18 - idade
        ano = dataAtul + saldo
        print('Ainda não precisa se alistar ao serviço militar neste ano de {}'.format(dataAtul))
        print('Faltam {} anos para o seu alistamento '.format(saldo))
        print('Seu alistamento vai ser no ano de {} '.format(ano))
# se é a hora exata de se alistar ou se já passou do tempo do alistamento.
    elif idade == 18:
        print('Neste ano de {} você já tem {} anos e precisar fazer o seu alistamento militar obrigatório'.format(dataAtul,idade))
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
    else:
        print('Neste {} ano, você tem {} anos e deveria ter se alistado no ano {}'.format(dataAtul,idade,dataAtul-(idade-18)))
else:
      print('O sexo FEMININO esta dispensada do serviço miloitar obrigatório!')
