#faça um program que leia um número de 0 a 9999
#e mostre na tela cada um dos digitos separados
núme = int(input('digite um número '))
unidade = núme // 1 % 10
dezena = núme // 10 % 10
centena = núme // 100 % 10
milhar = núme // 1000 % 10
print(' Unidade:{}\n Dezena:{}\n Centena:{}\n milhar:{}'.format(unidade, dezena, centena, milhar))

