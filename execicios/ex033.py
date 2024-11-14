#fazer um programar que leia três números e mostra qual o maior e qual é o menor
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o teceiro número: '))
#testando menor
menor = n1
if n2 < n3 and n2 < n1:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print('menor valor é {}'.format(menor))
#testando maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n2 and n3 > n1:
    maior = n3
print('maior valor é {}'.format(maior))





