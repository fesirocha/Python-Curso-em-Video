listaprincipal = []
while True:
    listaprincipal.append(int(input('Digite um valor: ')))
    op = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    while op not in 'SN':
        op = str(input('Comando inválido! Quer continuar [S/N]? ')).strip().upper()[0]
    if op == 'N':
        break
listapar = list()
listaimpar = []
for cont in listaprincipal:
    if cont % 2 == 0:
        listapar.append(cont)
    else:
        listaimpar.append(cont)
print('-='*20)
print(f'Lista completa: {listaprincipal}')
print(f'Lista de pares: {listapar}')
print(f'Lista impar: {listaimpar}')

