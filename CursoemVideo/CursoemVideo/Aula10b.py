n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota:'))
m = (n1+n2)/2
print('A sua média foi {}'.format(m))
print('PARABENS' if m >= 6 else 'REPROVADO')
