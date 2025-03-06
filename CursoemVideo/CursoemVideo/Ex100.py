from time import sleep
from random import randint
def sorteia(lst):
    print('Sorteando 5 valores da lista: ', end=' ')
    for c in range (0 ,5):
        lst.append(randint(0, 10))
        sleep(0.5)
        print(lst[c], end=' ')
    print('\nPRONTO!')
def somapar(lst):
    soma = 0
    for c in lst:
        if c % 2 == 0:
            soma += c
    sleep(1)
    print(f'Somando os valores pares de {lista}, temos {soma}')


lista = list()
sorteia(lista)
somapar(lista)