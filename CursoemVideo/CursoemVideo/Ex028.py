import random
from time import sleep
num = random.randint(1,5)
print('Vou pensar em um número de 0 a 5, tente adivinhar...') #Computador seleciona um numero aleatorio
esc = int(input('Descubra o número que o computador pensou (DE 1 A 5):')) #Usuário escolhe um numero
print('PROCESSANDO...')
sleep(2) #Tempo para dar emoção
print('PARABÉNS, VOCÊ DESCOBRIU O NÚMERO' if esc == num else 'Você perdeu MUAHAHA, o número era {}'.format(num)) #Condicional
