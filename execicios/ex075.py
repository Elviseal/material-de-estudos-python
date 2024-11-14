#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
# No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.
cont9 = c = 0
num = (int(input('digite um valor: ')), int(input('digite outro valor: ')), int(input('digite mais um valor: ')),
       int(input('digite ultimo valor: ')))

for c in range(0, len(num)):
       c += 1
       if num == 9:
              cont9 += 1

print(f'{c,cont9}')




