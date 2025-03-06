jogador = dict()
gols = []
time = list()
while True:
    numgols = 0
    jogador.clear()
    gols.clear()
    jogador['Nome'] = str(input('Nome do Jogador: '))
    partidas = int(input(f'Quantas partidas {jogador['Nome']} jogou? '))
    for c in range (1, partidas + 1):
        gol = int(input(f'Quantos gols na partida {c}? '))
        numgols += gol
        gols.append(gol)
    jogador['gols'] = gols.copy()
    jogador['Total de Gols'] = numgols
    time.append(jogador.copy())
#Se quer continuar ou não
    op = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    while op not in 'SN':
        op = str(input('Comando inválido! Quer continuar [S/N]? ')).strip().upper()[0]
    if op == 'N':
        break
print('-='*40)
print(f'{'Cód.':<5}{'Nome':<15}{'Gols':<15}{'Total':<5}')
print('-'*40)
for i, a in enumerate(time):
    print(f'{i:<5}', end='')
    for d in a.values():
        print(f'{str(d):<15}', end='')
    print()
print('-=' * 30)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {time[busca]['Nome']}')
        for i, g in enumerate(time[busca]['gols']):
            print(f'     No jogo {i+1} fez {g} gols')
    print('-'*40)
print('VOLTE SEMPRE')
