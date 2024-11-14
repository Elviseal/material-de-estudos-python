#condição simples
nome = input('digite seu nome ')
if nome == 'elvis':
    print('que nome lindo você tem!')
print('que nome comum você tem {}'.format(nome))
#condição composta
n1 = int(input('digite um número: '))
n2 = int(input('digite outro número: '))
m =(n1+n2)/2
if m >= 6:
    print('atingiu a média')
else:
    print('forá da média')
#condição simplificada ternário
print('na média' if m >=6.0 else'não atingiu a média')
