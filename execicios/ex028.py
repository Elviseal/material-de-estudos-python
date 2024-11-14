#jogo de adivinhar o número
import random
número = int(input('Adivinhe o número de 1 a 5:'))
lista =[1,2,3,4,5]
sorteio = random.choice(lista)
print('número sorteado foi {}'.format(sorteio))
if número == sorteio:
    print('Parabéns você acertou!!')
else:
    print('não foi dessa vez tente novamente!')

