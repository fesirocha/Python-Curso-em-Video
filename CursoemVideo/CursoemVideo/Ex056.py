#Nome, idade e sexo
mid = 0
velho = 0
nomevelho = 0
somamulheres = 0
for c in range(1, 5):
    print('------ {}ª PESSOA ------'.format(c))
    nome = str(input('Qual o nome? ')).strip()
    idade = int(input('Qual a idade? '))
    sexo = str(input('Qual o sexo? [M]/[F] ')).strip().upper()
    mid += idade
    if (sexo in 'M') and (idade > velho):
        velho = idade
        nomevelho = nome
    if (sexo in 'F') and (idade < 20):
        somamulheres += 1
#
print('A média de idade do grupo é de {}'.format(mid/4))
#
if nomevelho == 0:
    print('Não há homens para calcular a idade do mais velho')
else:
    print('O nome do homem mais velho é {}'.format(nomevelho))
#
print('{} mulheres tem menos de 20 anos'.format(somamulheres))



