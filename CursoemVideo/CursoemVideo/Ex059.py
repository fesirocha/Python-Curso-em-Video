#MENU
op = 0
n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
while op != 5:
    print('='*20)
    print('[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa')
    op = int(input('Digite a opção desejada: '))
    if op == 1:
        print('{} é o valor da soma dos dois números!'.format(n1+n2))
    elif op == 2:
        print('{} é a multiplicação dos dois números'.format(n1 * n2))
    elif op == 3:
        if n1 > n2:
            print('{} é o maior número'.format(n1))
        elif n2 > n1:
            print('{} é o maior número'.format(n2))
        else:
            print('Os dois números são iguais!')
    elif op == 4:
        n1 = int(input('Digite o 1º número: '))
        n2 = int(input('Digite o 2º número: '))
    elif op >= 6:
        print('OPÇÃO INVÁLIDA, TENTE NOVAMENTE!')
print('FIM')