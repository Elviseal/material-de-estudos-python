#calculo de preço de passagem, atravez da distância
distância = int(input('Digite a distância da viagem: '))
if distância <= 200:
    passagem = distância * .50
    print('Valor da passagem é R${:.2f} '.format(passagem))

else:
    passagem = distância * .45
    print('Valor da passagem é R${:.2f} '.format(passagem))
