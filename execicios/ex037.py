#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
númeroDecimal = int(input('Digite um número para converter: '))
opção = int(input(' Digite 1 para Binário \n Digite 2 para Octal \n Digite 3 para Hexadecimal '))
#1 para binário,
if opção == 1:
    print('O número {} em binário é {} '.format(númeroDecimal,bin(númeroDecimal)[2:]))
# 2 para octal
elif opção == 2:
    print('O número {} em octal é {} '.format(númeroDecimal,oct(númeroDecimal)[2:]))
# e 3 para hexadecimal.
elif opção == 3:
    print('O número {} em hexadecimal é {} '.format(númeroDecimal,hex(númeroDecimal)[2:]))
else:
    print('OPÇÃO INVALIDA!')