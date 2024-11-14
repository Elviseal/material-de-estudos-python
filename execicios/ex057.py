#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
#Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = str(input('Sexo [M/F] ')).strip()[0]#este [0] pega a primeira letra
while sexo not in 'FfMm':
     sexo = str(input(print('Dados inválidos. Por favor, informe o sexo: '))).strip().upper()[0]
print('Sexo {} registrado com sucesso! '.format(sexo))
