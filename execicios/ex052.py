#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
#ESSE PROGRAMA TIVE MUITA DIFICUDADE PARA FAZER E ACABEI COPIANDO
fim = int(input('Digite um número: '))
cores = {'limpa': '\033[m',
         'vermelho': '\033[31m',
         'amarelo': '\033[33m'
         }
cont = 0
for c in range(1, fim + 1):
    if fim % c == 0:
        print('{}'.format(cores['vermelho']), end='')
        cont += 1
    else:
        print('{}'.format(cores['amarelo']), end='')
    print('{}'.format(c), end=' ')
print('\n{}O númelo {} é divisível {} vezes'.format(cores['limpa'],fim, cont))
if cont == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO E PRIMO!')


