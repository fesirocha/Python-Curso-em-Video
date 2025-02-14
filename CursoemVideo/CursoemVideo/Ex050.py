#Ler 6 ns e somar os pares
s = 0
for c in range (1,7):
    n = int(input('Digite o {}º número: '.format(c)))
    if n % 2 == 0:
        s += n
print('A soma de todos os numeros pares digitados é de {}'.format(s))