#Crie um programa que leia a idade e o sexo de várias pessoas.
#A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
ida18 = munh20 = homens = 0
while True:
    idade = int(input('Qual a sua idade?  '))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Qual o seu sexo?[S/N] ')).upper().strip()[0]
    conti = ' '
    while conti not in 'SN':
        conti = str(input('Deseja continuar?[S/N] ')).upper().strip()[0]
    if conti == 'N':
        break
    if idade >= 18:
        ida18 += 1
    if sexo == 'F' and idade < 20:
        munh20 += 1
    if sexo == 'M':
        homens += 1


#A) quantas pessoas tem mais de 18 anos.
print(f'Foram cadastrados {ida18} maiores de 18 anos', end='')
#B) quantos homens foram cadastrados.
print(f' {homens} homens', end='')
#C) quantas mulheres tem menos de 20 anos.
print(f' e {munh20} munheres menores de 20 anos')