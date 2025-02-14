# BASE DE CONVERSÃO
n1 = int(input('Digite um numero inteiro: '))
print('Escolha uma das bases para conversão:')
print(' [1] BINÁRIO\n [2] OCTAL \n [3] HEXADECIMAL')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(n1, bin(n1)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(n1, oct(n1)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(n1, hex(n1)[2:]))
else:
    print('Opcao inválida. Tente novamente!')


