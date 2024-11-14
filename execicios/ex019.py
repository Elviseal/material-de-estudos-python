import random
a1 = input('primeiro Aluno: ')
a2 = input('segundo Aluno: ')
a3 = input('teceiro Aluno: ')
a4 = input('quarto Aluno: ')
lista =[a1, a2, a3, a4]
escolhido = random.choice(lista)
print('O aluno escolhido é :{} '.format(escolhido))
#atráves da importação da classe random e usando o metodo .choice é possível sotear nomes escritos anteriomente na lista