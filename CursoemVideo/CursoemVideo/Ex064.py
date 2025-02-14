soma = op = cont = 0
while op != 999:
    op = int(input('Digite um valor [999 para parar]: '))
    soma += op
    cont += 1
print('A soma total dos {} números digitados foi de {}'.format((cont-1), (soma - 999)))