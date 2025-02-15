num = [2, 5, 9, 1]
num[2] = 3
print(num)
num.append(7)
print(num)
num.sort()
print(num)
num.sort(reverse=True)
print(num)
num.insert(2, 0)
print(num)
num.pop()
print(num)
num.pop(2)
print(num)

valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('FIM!')

for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))
print(valores)