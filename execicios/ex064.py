#Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final,
# mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

soma = 0
mais = 0
cont = 0 #todas as variaves iniciadas junto, porque recebem o mesmo valor
mais = int(input('Digite um número [999 para parar]'))
while mais != 999:
    soma += mais
    cont += 1
    mais = int(input('Digite um número [999 para parar]'))
print('Foram digitados {} e a soma é {} '.format(cont, soma))



