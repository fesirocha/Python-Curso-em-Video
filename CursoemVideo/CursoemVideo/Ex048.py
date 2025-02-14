#Soma entre nº impares, multiplos de 3 entre 1 e 500
s = 0
for c in range (1, 501, 2):
    if c % 3 == 0:
        s += c
print('A soma é {}'.format(s))

