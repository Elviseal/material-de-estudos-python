salário = float(input('digite o salário do funcionário R$ '))
aumento = salário +(salário * 15/100)
print('um funcionário que recebe R${:.2f}, com aumento de 15% recebera R${:.2f}'.format(salário,aumento))
