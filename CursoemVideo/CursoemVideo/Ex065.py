op = 'S'
soma = total = n = maior = menor = 0
while op != 'N':
    n = int(input('Digite um número: '))
    soma += n
    total += 1
    if total == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    op = str(input('Quer continuar? [S/N] ')).upper()
print('A média dos {} valores digitados foi de {}'.format(total, (soma/total)))
print('{} foi o maior valor digitado e {} foi o menor'.format(maior, menor))
