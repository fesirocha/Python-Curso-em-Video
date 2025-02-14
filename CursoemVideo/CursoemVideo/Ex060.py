#Fatorial
from math import factorial
n1 = int(input('Digite um número: '))
f = n1
print('{}! = '.format(n1), end='')
while f != 1:
    print(' {} x'.format(f), end='')
    f -= 1
print(' 1 = {}'.format(factorial(n1)))