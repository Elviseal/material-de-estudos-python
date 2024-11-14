#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final,
#mostre os 10 primeiros termos dessa progressão.
i = int(input('Digite o primeiro termo da progressão: '))
p = int(input('Digite a razão da progressão: '))
cont = 0
print('O primeiro termo é :{}'.format(i))
print('A razão é :{}'.format(p))
print('O primeiro termos são: ')
pa = 0
de = i +(10 -1) * p
for c in range(i, de + p , p):
    cont += 1
    if cont <= 10:
        pa += p
        print('{}'.format(pa), end=' ')
print('Acabou!!')

#VERSÃO DO GUANABARA
print('\n{:=^60}'.format('versão curso em video'))
primeiro = int(input('Primeiro termo: '))
razão = int(input('razão: '))
decimo = primeiro +(10 - 1) * razão #para consegui o decimo número
for c in range(primeiro, decimo + razão, razão):
    print('{}'.format(c), end=' ')
print('ACABOU!!')