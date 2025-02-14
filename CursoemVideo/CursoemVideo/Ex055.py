#Pesos
maior = 0
menor = 0
for c in range (1, 6):
    peso = float(input('Digite o peso (Kg) da {}ª pessoa: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O menor peso foi de {} Kg e o maior peso foi de {} Kg'.format(menor, maior))