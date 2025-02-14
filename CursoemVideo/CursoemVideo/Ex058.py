#Jogo do acertar o numero
from random import randint
from time import sleep
computador = randint(0, 10)
print('Eu vou pensar em um número de 0 a 10!!')
print('PENSANDO...')
sleep(2)
print('\033[1;34mTENTE DESCOBRIR QUAL É\033[m')
sleep(0.5)
escolha = int(input('\033[1;31mESCOLHA SEU PALPITE: \033[m'))
vezes = 0
while escolha != computador:
    print('VOCÊ ERROU!')
    if escolha > computador:
        escolha = int(input('\033[1;31mMENOS.....TENTE MAIS UMA VEZ! ESCOLHA SEU PALPITE: \033[m'))
        vezes += 1
    else:
        escolha = int(input('\033[1;31mMAIS.....TENTE MAIS UMA VEZ! ESCOLHA SEU PALPITE: \033[m'))
        vezes += 1
print('='*40)
print('PARABÉNS! VOCÊ DESCOBRIU!!!')
print('Você precisou de {} tentativa(s) para descobrir'.format(vezes))