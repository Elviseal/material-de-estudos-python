#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
#na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time da Chapecoense.
tabela = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo', 'Atlético-MG', 'Athletico-PR', 'Cruzeiro',
          'Botafogo', 'Santos', 'Bahia', 'Fluminense', 'Corinthians', 'Chapecoense', 'Ceará', 'Vasco', 'América-MG',
          'Sport', 'Vitória', 'Paraná')
print('{:=^60}'.format(' CLASSIFICAÇÃO DOPS TIMES '))
print(f'{tabela}')
print('{:=^60}'.format(' 5 PRIMEIROS CLASSIFICADOS '))
print(f'{tabela[0:5]}')
print('{:=^60}'.format(' 4 ÚLTIMOS '))
print(f'{tabela[-4:]}')
print('{:=^60}'.format(' TIMES EM ORDEM ALFABETICA'))
print(sorted(tabela))
print('{:=^60}'.format(' POSIÇÃO DA  CHAPECOENSE '))
print(f'A Chapecoense esta na posição {tabela.index('Chapecoense')+1}ª do capionato')






