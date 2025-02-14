# REFAZER O EXERCÍCIO 35
l1 = float(input('Digite um lado do triangulo: '))
l2 = float(input('Digite o segundo lado do triangulo: '))
l3 = float(input('Digite o terceiro lado do triangulo: '))
if (l1 < l2 + l3) and (l2<l1+l3) and (l3<l1+l2):
    print('Essas tres retas podem formar um triangulo!')
    if (l1 == l2) and (l1 == l3):
        print('O triângulo formado é um triângulo equilátero, no qual todos os lados são iguais')
    elif l1 != l2 != l3 != l1:
        print('O triângulo formado é um triângulo escaleno, no qual todos os lados são diferentes')
    else:
        print('O triãngulo formado é um triângulo isósceles, no qual dois lados são iguais')
else:
    print('Essas tres retas nao podem formar um triangulo!')