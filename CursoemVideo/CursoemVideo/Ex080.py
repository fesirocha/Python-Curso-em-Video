lista = []
for numeros in range (0, 5):
    num = int(input('Digite um número para ser adicionado a lista: '))
    if numeros == 0 or num > lista[-1]:
        lista.append(num)
        print(f'Adicionado na última posição da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                print(f'Valor adicionado na posição {pos}')
                break
            pos += 1
print(lista)
