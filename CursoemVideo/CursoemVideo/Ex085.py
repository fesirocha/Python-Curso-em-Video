numeros = [[],[]]
num = 0
for c in range(0, 7):
    num = (int(input(f'Digite o {c + 1}º valor: ')))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)
numeros[0].sort()
numeros[1].sort()
print(f'Os valores ímpares digitados foram: {numeros[1]}')
print(f'Os valores pares digitados foram: {numeros[0]}')