matriz = list()
for i in range (0 , 3):
    for j in range (0, 3):
        matriz.append(int(input(f'Digite um valor para [{i}, {j}]: ')))
for c in range(0, len(matriz), 3):
    print(f'[{matriz[c]:^6}] [{matriz[c+1]:^6}] [{matriz[c+2]:^6}]')
