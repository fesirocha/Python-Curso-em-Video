numeros = ('zero', 'um', 'dois', 'três', 'quatro',
           'cinco', 'seis', 'sete', 'oito', 'nove',
           'dez', 'onze', 'doze', 'treze', 'quatorze',
           'quinze', 'dezesseis', 'dezessete',
           'dezoito', 'dezenove', 'vinte')
op = 'A'

while True:
    usuario = int(input('Digite um numero entre 0 e 20: '))
    while (usuario < 0) or (usuario > 20) :
        usuario = int(input('Tente novamente! Digite um numero entre 0 e 20: '))
    print(f'Você digitou o numero {numeros[usuario]}')
    op = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    while op not in 'SN':
        op = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if op == 'N':
        break
