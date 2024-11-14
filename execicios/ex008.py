metros = float(input('digite o valor que quer converte:'))
km = metros * 0.001
hm = metros * 0.01
dam = metros * 0.1
m = metros
dm = metros * 10
cm = metros * 100
mm = metros * 1000
print('A converção do número digitado em:\nQuilômetro: {:.3f}km\nHectômetro: {:.2f}hm\nDecâmetro: {:.1f}dam\nMetro: {:.2f}m'.format(km,hm,dam,m))
print('Decimetro: {:.0f}dm\n Centimetro: {:.0f}cm\n Milimetro: {:.0f}mm'.format(dm,cm,mm))
#quilômetro (km)	hectômetro (hm)	decâmetro (dam)	metro (m)	decímetro (dm)	centímetro (cm)	milímetro (ml)
