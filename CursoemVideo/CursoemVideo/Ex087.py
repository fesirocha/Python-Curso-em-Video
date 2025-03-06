matriz = list()
somapar = somacoluna = maior_valor = 0
#Criar a matriz
for l in range (0, 3):
    for c in range (0, 3):
        matriz.append(int(input(f'Digite o valor [{l}] [{c}]: ')))
print('-='*20)
#Mostrar a matriz formatada
for num in range(0, len(matriz), 3):
    print(f'[{matriz[num]:^5}][{matriz[num+1]:^5}][{matriz[num+2]:^5}]')
print('-='*20)
#Somar os numeros pares
for par in matriz:
    if par % 2 == 0:
        somapar += par
print(f'A soma dos valores pares é {somapar}')
#Somar os numeros da terceira coluna
for soma in matriz[2::3]:
    somacoluna += soma
print(f'A soma dos valores da terceira coluna é {somacoluna}')
#Verificar o maior numero da segunda linha
maior_valor = max(matriz[3:6])
print(f'O maior valor da segunda linha é {maior_valor}')


