#Tabuada
while True:
    print('\033[1;31m-\033[m'*40)
    n = int(input('Quer ver a tabuada de qual valor: '))
    print('\033[1;31m-\033[m'*40)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
print('TABUADA ENCERRADA!')
