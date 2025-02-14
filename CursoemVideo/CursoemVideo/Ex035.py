l1 = float(input('Digite um lado do triangulo: '))
l2 = float(input('Digite o segundo lado do triangulo: '))
l3 = float(input('Digite o terceiro lado do triangulo: '))

if (l1<l2+l3) and (l2<l1+l3) and (l3<l1+l2):
    print('Essas tres retas podem formar um triangulo! ')
else:
    print('Essas tres retas nao podem formar um triangulo!')