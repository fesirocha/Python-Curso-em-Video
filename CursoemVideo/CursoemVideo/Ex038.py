# LEITOR DE VALORES
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor:'))
if n1 > n2:
    print('O primeiro valor ({}) é maior'.format(n1))
elif n2 > n1:
    print('O segundo valor ({}) é maior'.format(n2))
else:
    print('Não existe valor maior, os dois são iguais ({})'.format(n1))
