#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
#No final do programa, mostre:
#a média de idade do grupo,
#qual é o nome do homem mais velho
#e quantas mulheres têm menos de 20 anos.
#este tive muita dificudade nas inicializações das variaveis
idaVelho = 0
nomevelho =''
totFe = 0
totid = 0
for pessoas in range(1, 5):
    print('{:-^20}'.format(' {}ª PESSOA '.format(pessoas)))
    nome = str(input('NOME: ')).strip().upper()
    idade = int(input('IDADE: '))
    sexo = str(input('[M/F]: ')).strip()
    totid += idade
    if pessoas == 1 and sexo in 'mM': #inicia as variaveis
         idaVelho = idade
         nomevelho = nome
    if sexo in 'Mm' and idade > idaVelho:
        idaVelho = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totFe += 1
media = totid / pessoas
print('Á média de idade do grupo é de {} anos'.format(media))
print('O homem mais velho tem {} anos e se chama {} '.format(idaVelho, nomevelho))
print('Ao total são {} mulheres com menos de 20 anos'.format(totFe))

