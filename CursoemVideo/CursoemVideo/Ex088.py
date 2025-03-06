from random import randint
from time import sleep
print('-' * 40)
print(f'{'JOGA NA MEGA SENA':^40}')
print('-' * 40)
jogos = list()
temp = list()
num = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 0
while tot < num:
    cont = 0
    while True:
        numero = randint(1, 60)
        if numero not in temp:
            temp.append(numero)
            cont += 1
        if cont >= 6:
            break
    tot += 1
    temp.sort()
    jogos.append(temp[:])
    temp.clear()
#Mostrando os jogos
print('-=' * 3,f' SORTEANDO {num} JOGOS ', '-=' * 3)
for i, lista in enumerate(jogos, start=1):
    print(f'Jogo {i}: {lista}')
    sleep(1)
print('-=' * 5, f' BOA SORTE!', '-=' * 5)



