from math import hypot
#importando o classe math
co = float(input('digite o cateto oposto: '))
ca = float(input('digite o cateto adjacente: '))
print('o cateto oposto vale {} \n o cateto adjacente {} \n e sua hipotenusa {:.2f}'.format(co, ca, hypot(co, ca)))

#fomula matematica
hi = (co ** 2 + ca ** 2) ** (1/2)
print('sem metodo hypot {:.2f}'.format(hi))
