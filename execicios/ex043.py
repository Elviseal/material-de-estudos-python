#Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
#calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
altura = float(input('Digite sua altura em metros: '))
peso = float(input('Digite seu peso: '))
imc = peso / (altura ** 2)
print('Seu IMC é {:.2f} e seu peso esta '.format(imc), end='')
#– IMC abaixo de 18,5: Abaixo do Peso
if imc < 18.5:
    print('Abaixo do Peso')
#– Entre 18,5 e 25: Peso Ideal
elif imc < 25:
    print('Peso Ideal')
#– 25 até 30: Sobrepeso
elif imc < 30:
    print('Sobrepeso')
#– 30 até 40: Obesidade
elif imc < 40:
    print('Obesidade')
#– Acima de 40: Obesidade Mórbida
else:
    print('Obesidade Mórbida')
