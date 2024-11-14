#analisa se no nome tem silva
nome = str(input('Qual seu nome completo ?'.capitalize())).strip()
print('seu nome tem silva: {}'.capitalize().format('silva'.upper() in nome.upper()))
