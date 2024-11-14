#Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.
primeiro = int(input('Digite o primeiro termo da PA: '))
razão = int(input('Digite a razão: '))
cont = 1
pa = primeiro
total = 0
maispa = 10
while maispa != 0:
    total = total + maispa
    while cont <= total:
        print('{}'.format(pa), end=' ')
        pa += razão
        cont += 1
    print('pausa')
    maispa = int(input('quantos termos deseja mostrar agora: '))
print('total de {} termos '.format(total))
#
#progressão finalizada com tantos termos mostrados
