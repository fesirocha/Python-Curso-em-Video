# CONTAGEM DE 1 A 6
for c in range(1, 7):
    print(c)
print('Fim')

# CONTAGEM DE 6 A 1
for c in range(6, 0, -1):
    print(c)
print('Fim')

# CONTAGEM DE 0 A 6 DE 2 EM 2
for c in range(0, 7, 2):
    print(c)
print('Fim')

# CONTAGEM DE 0 AO Nº DIGITADO
#n = int(input('Digite um nº: '))
#for c in range (0, n+1):
#        print(c)
#print('FIM')

# SOMATÓRIO DE N NUMEROS
s = 0
n = int(input('Quantos numeros vc quer digitar? '))
for c in range(0, n):
    a = int(input('Digite um valor a ser somado: '))
    s += a
print('A soma de todos os numeros é de {}'.format(s))
