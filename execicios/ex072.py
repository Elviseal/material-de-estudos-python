#Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Deis', 'Onze', 'Doze',
           'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezesete', 'Dezoito', 'dezenove', 'Vinte')

while True:
    numero = int(input('Digite um numero entre 0 e 20:'))
    if 0 <= numero <= 20:
        print(f'O numero {numero} por extenso é {extenso[numero]}')
    if numero <= 0 or numero >= 20:
        print('Tente novamento.', end=' ')
    else:
        conti = ' '
        while conti not in 'SN':
            conti = str(input('Quer continuar? [S/N]')).upper().strip()[0]
        if conti == 'N':
            break







