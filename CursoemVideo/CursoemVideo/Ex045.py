# JOGO DE PEDRA, PAPEL E TESOURA
from random import randint
from time import sleep
itens = ('PEDRA', 'PAPEL', 'TESOURA')
print('\033[1;31m{:=^40}\033[m'.format(' JOKENPÔ '))
print('''\033[0;35m[0]\033[m PEDRA
\033[0;35m[1]\033[m PAPEL
\033[0;35m[2]\033[m TESOURA''')
op = int(input('\033[1;;45mFAÇA A SUA JOGADA: \033[m '))
pc = randint(0,2)
print('JO')
sleep(0.6) #Tempo para dar emoção
print('KEN')
sleep(0.6) #Tempo para dar emoção
print('PÔ')
sleep(0.6) #Tempo para dar emoção

print ('\033[0;33mEU ESCOLHI {}\033[m'.format(itens[pc]))
sleep(0.8) #Tempo para dar emoção
print('=' * 20)
if op == 0: #jogador jogou Pedra
    if pc == 0:
        print('\033[0;33mPORTANTO, EMPATOU.\033[m')
    elif pc == 1:
        print('\033[1;;41mGANHEI, PAPEL COBRE A PEDRA!\033[m')
    else:
        print('\033[1;;42mPARABÉNS, VOCÊ GANHOU! PEDRA QUEBRA MINHA TESOURA\033[m')
elif op == 1: #jogador jogou Papel
    if pc == 1:
        print('\033[0;33mPORTANTO, EMPATOU.\033[m')
    elif pc == 2:
        print('\033[1;;41mGANHEI, MINHA TESOURA CORTA O SEU PAPEL!\033[m')
    else:
        print('\033[1;;42mPARABÉNS, VOCÊ GANHOU! SEU PAPEL COBRE MINHA PEDRA!\033[m')
elif op == 2: #jogador jogou Tesoura
    if pc == 2:
        print('\033[0;33mPORTANTO, EMPATOU.\033[m')
    elif pc == 0:
        print('\033[1;;41mGANHEI! MINHA PEDRA QUEBRA SUA TESOURA!\033[m')
    else:
        print('\033[1;;42mPARABÉNS, VOCÊ GANHOU! SUA TESOURA CORTA O MEU PAPEL\033[m')
else:
    print('OPÇÃO INVÁLIDA. REINICIE O JOGO!')
print('=' * 20)


