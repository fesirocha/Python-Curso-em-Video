lista = []
cont = 0
while True:
    lista.append(int(input('Digite um valor: ')))
    cont += 1
    op = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    while op not in 'SN':
        op = str(input('Comando inválido! Quer continuar [S/N]: ')).strip().upper()[0]
    if op in 'N':
        break
print('-='*20)
print(f'Foram digitados {cont} elementos')
lista.sort(reverse=True)
print(f'A lista ordenada na ordem inversa: {lista}')
if 5 in lista:
    print(f'O valor 5 foi digitado e está na posição {lista.index(5)}')
else:
    print(f'O valor 5 não foi digitado')
