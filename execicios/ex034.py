#almento de salário de 15% para quem recebe menos de 1250,00 e de 10% para outros
salario = float(input('Qual o seu salário ? R$ '))
if salario > 1250.00:
    salario = salario + (salario * 10/100)
    print(f'Seu novo salário é R${salario}')
else:
    Salario = salario + (salario * 15/100)
    print('Seu novo salário é R${}'.format(Salario))