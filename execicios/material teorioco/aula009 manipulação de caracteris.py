frase = 'curso em video python'
#fatiamento
print(frase[9]) #pega só a letra do índice 9
print(frase[9:13]) #começa índice 9 até 13, mas não entra o ultimo valor
print(frase[9:21:2]) #começa índice 9 até 21 saltando de 2 em 2, mas não entra o ultimo valor
print(frase[:5])# começa do índice 0 até 5
print(frase[15:])#começa índece 15 até final
print(frase[9::3])#começa no índice 9 até o final de 3 em 3
#análise
print(len(frase))#comprimento
print(frase.count('o'))#conta quantos vezes aparece o 'o'
print(frase.count('o',0,13))#conta e fatia quantas vezes aparece o 'o' do índice 0 até 13
print(frase.find('deo'))#mostra a posição onde começa o 'deo', quando não tiver vaio retornar false
print('curso' in frase)#esse operador verificar se tem a palavras 'curso'
#transformação
print(frase.replace('python','android'))#troca as palavras indicadas
print(frase.upper())#escreve tudo em maiúscula
print(frase.lower())#escreve tudo em minuscular
print(frase.capitalize())#escreve só a primeira letras ficar maiúscula
print(frase.title())#a primeira letra de cada palavras maiúscula
print(frase.strip())#remove os espaços inúteis, com variação no começo 'r' para direita e 'l' para esquerda
#divisão
print(frase.split())#divisão em listas das palavras ou frases , criando um novo indice
#junção
print('-'.join(frase))#vai juntar usando o '-'
sorted()metodo de colocar em ordem alfabetica

