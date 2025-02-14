#Fibonacci
n = int(input('Quantos termos você quer mostrar: '))
c = 0
t1 = 0
t2 = 1
apoio = 0
while c < n:
    c += 1
    print('{} -> '.format(t1), end='')
    apoio = t2
    t2 = t1 + t2
    t1 = apoio
print('Fim')
