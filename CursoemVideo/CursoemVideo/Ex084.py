pessoas = list()
apoio = list()
op = ''
pesado = leve = cont = 0
while True:
    apoio.append(str(input('Digite o nome: ')))
    apoio.append(float(input('Digite o peso (kg): ')))
    pessoas.append(apoio[:])
    apoio.clear()
#Se usuário quer continuar ou não
    op = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    while op not in 'SN':
        op = str(input('Comando inválido! Quer continuar [S/N]? ')).strip().upper()[0]
    if op in 'N':
        break
#Após o break, para avaliar a lista das pessoas
for p in pessoas:
    cont += 1
    if cont == 1:
        pesado = p[1]
        leve = p[1]
    else:
        if p[1] > pesado:
            pesado = p[1]
        elif p[1] < leve:
            leve = p[1]
print('-='*20)
print(f'Você cadastrou {cont} pessoas no sistema...')
#verificar mais pesados
print(f'As pessoas mais pesadas foram cadastradas com {pesado} kg. São elas: ', end='')
for peso in pessoas:
    if peso[1] == pesado:
        print(f'{peso[0]} ', end='')
#verificar mais leves
print(f'\nAs pessoas mais leves foram cadastradas com {leve} kg. São elas: ', end='')
for peso in pessoas:
    if peso[1] == leve:
        print(f'{peso[0]} ', end='')
