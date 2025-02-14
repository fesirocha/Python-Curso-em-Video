#Par ou Impar
from random import randint
from time import sleep
jogador = computador = soma = cont = 0
opcao = valor = ' '
print('Oi, sou seu \033[1;32mCOMPUTADOR\033[m e quero jogar \033[1;32mPAR\033[m ou \033[1;32mIMPAR\033[m!!\033[m')
while True:
    computador = randint(0, 5)
    jogador = int(input('Vou escolher um número! Escolha o seu: '))
    while opcao not in 'PI':
        opcao = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()[0]
    soma = jogador + computador
    #Verificando se é PAR ou IMPAR
    if soma % 2 == 0:
        valor = 'P'
    else:
        valor = 'I'
    #Verificando quem venceu
    if opcao == valor:
        print('PROCESSANDO...')
        sleep(1)
        print('-'*40)
        print(f'Eu escolhi {computador} e você {jogador}. A soma é {soma}. ', end='')
        print('DEU PAR' if valor == 'P' else 'DEU ÍMPAR')
        print('Você venceu, parabéns!! Continue jogando')
        print('-' * 40)
        cont += 1
    else:
        print('PROCESSANDO...')
        sleep(1)
        print('-' * 40)
        print(f'Eu escolhi {computador} e você {jogador}. A soma é {soma}. ', end='')
        print('DEU PAR' if valor == 'P' else 'DEU ÍMPAR')
        print(f'PERDEU! Voce ganhou {cont} vezes seguidas!')
        print('-' * 40)
        break

