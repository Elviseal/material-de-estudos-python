dias = int(input('quantos dias o carros foi alugado: '))
km = float(input('quantos km rodados: '))
aluguel = dias * 60 + km * 0.15
print('total a pagar é R${:.2f}'.format(aluguel))
  