#Primeiro termo e razão da PA
n = int(input('Digite o primeiro terma da PA: '))
r = int(input('Digite a razão da PA: '))
dez = n + (10-1) * r
for c in range (n, dez + r, r):
    print(c, end=' -> ')
print('ACABOU')