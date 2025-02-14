#Lojinha
prodbarato = ' '
soma = mais1000 = menor = cont = 0
while True:
    print('-'*40)
    print(f'{'LOJINHA!!':^40}')
    print('-'*40)
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    cont += 1
    soma += preco
    if preco > 1000:
        mais1000 += 1
    if cont == 1 or preco < menor:
        menor = preco
        prodbarato = produto
    op = ' '
    while op not in 'SN':
        op = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if op in 'Nn':
        break
print('-'*10, 'COMPRA EFETUADA!!!', '-'*10)
print(f'O total da compra foi de R${soma}')
print(f'temos {mais1000} produtos custando mais de R$1000')
print(f'O produto mais barato foi {prodbarato} que custou R${menor}')
