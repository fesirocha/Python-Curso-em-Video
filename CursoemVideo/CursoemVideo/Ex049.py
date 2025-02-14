#Tabuada
n=int(input('Escolha um nº para a tabuada: '))
print('-'*15)
print('TABUADA DO {}'.format(n))
for c in range (0 , 11):
    print('{} X {} = {}'.format(n, c, (n*c)))