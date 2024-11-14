#Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2)/2
cores = {'limpa':'\033[m',
         'vermelho':'\033[31m',
         'azul':'\033[34m',
         'amarelo':'\033[33m'}
print('Com as notas {} e {} sua média é {} '.format(nota1, nota2, media))
#– Média abaixo de 5.0: REPROVADO
if media <= 5.0:
    print('{}Aluno REPROVADO!{}'.format(cores['vermelho'], cores['limpa']))
#– Média entre 5.0 e 6.9: RECUPERAÇÃO
elif media >= 5.0 and media < 7.0:
    print('{}Aluno em RECUPERAÇÃO!{}'.format(cores['amarelo'], cores['limpa']))
#– Média 7.0 ou superior: APROVADO
else:
   print('{}Aluno APROVADO!{}'.format(cores['azul'], cores['limpa']))
