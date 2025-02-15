lista = []
op = ''
while True:
    num = int(input('Digite um valor: '))
    if num in lista:
        print('Valor duplicado! Não vou adicionar...')
    else:
        lista.append(num)
        print('Valor adicionado com sucesso!')
    op = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    #Esse while abaixo é só para caso o usuário digite algo fora de Não ou Sim
    while op not in 'SN':
        op = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if op in 'N':
        break
print('-='*20)
lista.sort()
print(f'Você digitou os valores {lista}')
