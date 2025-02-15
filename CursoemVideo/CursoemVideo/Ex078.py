lista = []
for cont in range (1,6):
    lista.append(int(input(f'Digite o {cont}º valor: ')))
print(f'Os valores digitados foram {lista}')
print(f'O maior valor digitado foi {max(lista)} e a posição dele é ', end='')
for i, v in enumerate(lista):
    if v == max(lista):
        print(f'{i}...', end='')
print('')
print(f'O menor valor digitado foi {min(lista)} e a posição dele é ', end='')
for i, v in enumerate(lista):
    if v == min(lista):
        print(f'{i}...', end='')
print('')
