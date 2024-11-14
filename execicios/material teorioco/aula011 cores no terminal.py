#CORES NO PADRÃO ANSI \033[m
#\033 começo do código para mudar as cores
print('O primeiro número depois do colchete é o STYLE')
print('\033[0m 0 sem style\033[m')
print('\033[1m 1 negrito\033[m')
print('\033[4m 4 sublinhado\033[m')
print('\033[7m 7 inverter text pelo back\033[m')
print('O segundo númemo é o TEXT')
print('\033[30m 30 branco\033[m')
print('\033[31m 31 vermelho\033[m')
print('\033[32m 32 verde\033[m')
print('\033[33m 33 amarelo\033[m')
print('\033[34m 34 azul\033[m')
print('\033[35m 35 magenta\033[m')
print('\033[36m 36 siano\033[m')
print('\033[37m 37 cinza\033[m')
print('O terceiro número é o BACK')
print('\033[40m 40 branco\033[m')
print('\033[41m 41 vermelho\033[m')
print('\033[42m 42 verde\033[m')
print('\033[43m 43 amarelo\033[m')
print('\033[44m 44 azul\033[m')
print('\033[45m 45 magenta\033[m')
print('\033[46m 46 siano\033[m')
print('\033[47m 47 cinza\033[m')
#manipulando as cores usando o format
nome = 'elvis'
print('olá, Muito prazer em te conhecer!!! {}{}{}'.format('\033[4;34m', nome, '\033[m'))
#criando coleções
cores ={ 'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;40m'}
print('olá, Muito prazer em te conhecer!!! {}{}{}'.format(cores['pretoebranco'], nome, cores['limpa']))

