def ficha(nome='', gols=0):
    if nome == '':
        nome = '<desconhecido>'
    if gols == '':
        gols = 0
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato!')
jogador = str(input('Nome do jogador: '))
gols = input('Nº de gols: ')
ficha(jogador, gols)