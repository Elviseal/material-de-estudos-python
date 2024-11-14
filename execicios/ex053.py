#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
#APOS A SOPA,
#A SACADA DA CASA,
#A TORRE DA DERROTA,
#O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
frase = str(input('Digite a frase: ')).strip().upper()
palavras = frase.split()
junta = ''.join(palavras)
print('Você digitou a {}'.format(junta))
if junta[::-1] == junta:
    print('Essa frase é POLÍNDROMO!')
else:
    print('Essa frase NÃO É UM POLÍDROMO!')


