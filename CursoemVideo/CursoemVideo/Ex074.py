from random import randint
lista = (randint(1,10), randint(1,10),randint(1,10), randint(1,10), randint(1,10))
print('Os valores sorteados foram: ', end='')
for n in lista:
    print(f'{n} ', end='')
print(f'\nO menor valor sorteado foi de {min(lista)}')
print(f'O maior valor sorteado foi de {max(lista)}')

