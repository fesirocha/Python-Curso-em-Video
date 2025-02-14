# ALISTAMENTO NO EXÉRCITO
from datetime import date
nasc = int(input('Em que ano você nasceu? '))
dif = date.today().year - nasc
if dif < 18:
    print('O usuário ainda vai se alistar no exército')
    print('Faltam cerca de {} ano(s) para o alistamento'.format(18 - dif))
elif dif > 18:
    print('O usuário já deveria ter se alistado no exército')
    print('O prazo passou há cerca de {} ano(s)'.format(dif-18))
else:
    print('É hora do usuário se alistar no exército!')