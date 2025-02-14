#TUPLAS
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche)
print(lanche[1])
print('*'*10)
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('*'*10)
print(lanche[-1])
print('*'*20)

for cont in range(0, len(lanche)):
    print(f'VOU COMER {lanche[cont]}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')