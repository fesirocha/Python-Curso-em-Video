#Fatorial Melhorado
pt = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
termo = pt
cont = 1
mais = 10
total = 0
while mais != 0:
    total += mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += r
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('FIM!')
