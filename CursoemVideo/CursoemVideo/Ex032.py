from datetime import date
ano = int(input('Digite um ano (coloque 0 para analisar o ano atual): '))
if ano == 0:
    ano = date.today().year
print('{} é um ano bissexto'.format(ano) if (ano % 4 ==0) and (ano%100 != 0) or (ano%400 == 0) else '{} não é um ano bissexto'.format(ano))
