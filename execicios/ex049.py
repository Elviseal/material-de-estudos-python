#Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando um laço for.
n = int(input('digite um número para ser multiplicado: '))
for c in range(0, 11):
    print('{} x {} = {}'.format(n,c, n * c))

