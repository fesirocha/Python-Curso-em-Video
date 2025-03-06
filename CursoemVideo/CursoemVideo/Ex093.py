jogador = dict()
gols = []
numgols = 0
jogador['Nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {jogador['Nome']} jogou? '))
for c in range (1, partidas + 1):
    gol = int(input(f'Quantos gols na partida {c}? '))
    numgols += gol
    gols.append(gol)
jogador['gols'] = gols.copy()
jogador['Total de Gols'] = numgols
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador['Nome']} jogou {partidas} partidas')
for c in range(0, partidas):
    print(f'=> Na partida {c+1}, fez ', end='')
    if gols[c] <= 1:
        print(f'{gols[c]} gol!!')
    else:
        print(f'{gols[c]} gols!!')

