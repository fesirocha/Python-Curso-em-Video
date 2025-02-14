km = float(input('Qual a distância da sua viagem? (em km) '))
if km <= 200:
    print('O preço da sua passagem é de R${}'.format(km*0.5))
else:
    print('O preço da sua passagem é de R${}'.format(km*0.45))
