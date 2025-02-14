# CATEGORIAS NATAÇÃO
from datetime import date
nasc = int(input('Qual o ano de nascimento do atleta? '))
dif = (date.today().year - nasc)
if dif <= 9:
    print('IDADE: {} - CATEGORIA: MIRIM - ATÉ 9 ANOS'.format(dif))
elif dif <= 14:
    print('IDADE: {} - CATEGORIA INFANTIL - ATÉ 14 ANOS'.format(dif))
elif dif <= 19:
    print('IDADE: {} - CATEGORIA JUNIOR - ATÉ 19 ANOS'.format(dif))
elif dif <= 25:
    print('IDADE: {} - CATEGORIA SÊNIOR - ATÉ 25 ANOS'.format(dif))
else:
    print('IDADE: {} - CATEGORIA MASTER - ACIMA DE 25 ANOS'.format(dif))