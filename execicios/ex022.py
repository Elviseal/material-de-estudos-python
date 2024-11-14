nome = str(input('Digite seu nome completo: ')).strip()#remove os espaços
print('Analisando seu nome...')
print('Seu nome em maiúsculo é {}'.format(nome.upper()))#letras maiúculas
print('Seu nome em minúsculo é {}'.format(nome.lower()))#letras minúsculas
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))#len conta as letras e o count conta oque esta entre ''
separa = nome.split()#transforma em lista
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0],len(separa[0])))
