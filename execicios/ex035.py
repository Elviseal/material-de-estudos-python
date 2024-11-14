#verificando se segmentos de retas podem ser triangulos
#a soma de dois seguimentos nunca pode ser maior que o terceiro
reta1 =int(input('Digite o primeiro segmento de reta: '))
reta2 =int(input('Digite o segundo segmento de reta: '))
reta3 =int(input('Digite o terceiro segmento de reta: '))
if reta1 + reta2 > reta3 and reta2 + reta3 > reta1 and reta3 + reta1 > reta2:
    print('Esses segmenetos podem forma um triângulo ')
else:
    print('Como esses segmentos não é possível montar um triângulo')
