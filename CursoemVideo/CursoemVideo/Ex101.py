def eleicao (y=0):
    from datetime import date
    idade = date.today().year - y
    if idade < 16:
        print(f'Com {idade} anos: NÃO VOTA!')
    elif 18 <= idade < 65:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO!')
    else:
        print(f'Com {idade} anos: VOTO OPCIONAL!')
print('-'*20)
ano = int(input('Em que ano você nasceu? '))
eleicao(ano)
