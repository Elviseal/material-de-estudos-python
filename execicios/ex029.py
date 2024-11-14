#multa de velocidade acima de 80km
velocidade = float(input('Qual á velocidade? '))
if velocidade > 80:
    multa = (velocidade - 80) * 7.0
    print('Sua velocidade é de {}km'.format(velocidade))
    print('Multa por velocidade superior a 80km {:.2f} reais'.format(multa))
print('Sua velocidade {}km\n Boa viagem!'.format(velocidade))


