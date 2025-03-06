from random import randint
from time import sleep
from operator import itemgetter
dados = {}
list = []
for c in range (1 , 5):
    dados['nome'] = f'Jogador {c}'
    dados['numero'] = randint(1, 6)
    list.append(dados.copy())
print('Valores sorteados:')
for c in range (0, len(list)):
    print(f'O {list[c]["nome"]} tirou {list[c]["numero"]}')
    sleep(1)
print('Ranking dos jogadores:')
lista_ordenada = sorted(list, key = lambda p: p["numero"], reverse = True)
for c in range (0, len(lista_ordenada)):
    print(f'O {lista_ordenada[c]["nome"]} tirou {lista_ordenada[c]["numero"]}')