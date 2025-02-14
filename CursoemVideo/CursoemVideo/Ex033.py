n1 = int(input('Digite um primeiro numero: '))
n2 = int(input('Digite um segundo numero: '))
n3 = int(input('Digite um terceiro numero: '))
ap = 0
if n1 > n2:
    ap = n1
    n1 = n2
    n2 = ap
if  n1 > n3:
    ap = n1
    n1 = n3
    n3 = ap
if n2 > n3:
    ap = n2
    n2 = n3
    n3 = ap

print ('O menor valor digitado foi {} e o maior valor foi {}'.format(n1, n3))

