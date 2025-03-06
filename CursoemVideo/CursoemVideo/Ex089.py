boletim = list()
while True:
#Entrada dos dados em loop infinito
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2)/2
    boletim.append([nome, [n1, n2], media])
#pergunta se quer continuar ou não
    op = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    while op not in 'SN':
        op = str(input('Comando inválido!! Quer continuar [S/N]? ')).strip().upper()[0]
    if op == 'N':
        break
print('-='*40)
print(f'{'Nº':<3}', f'{'NOME':<15}', f'{'MÉDIA':^12}')
print('-'*30)
for i, a in enumerate(boletim):
    print(f'{i:<3}{a[0]:<15}{a[2]:^15.1f}')
while True:
    print('-'*30)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(boletim) - 1:
        print(f'Notas de {boletim[opc][0]} são {boletim[opc][1]}')
