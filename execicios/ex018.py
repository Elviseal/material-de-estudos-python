from math import sin,cos,tan,radians
ângulo = float(input('digite o ângulo desejado: '))
seno = sin(radians(ângulo))
print('o ângulo {} tem o SENO de {:.2f}'.format(ângulo,seno))
cosseno = cos(radians(ângulo))
print('o ângulo {} tem o COSSENO de {:.2f}'.format(ângulo,cosseno))
tangente = tan(radians(ângulo))
print('o ângulo {} tem a TANGENTE de {:.2f}'.format(ângulo,tangente))

