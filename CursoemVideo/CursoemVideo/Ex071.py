#Caixa Eletronico
print('='*40)
print(f'{'BANCO LELEK':^40}')
print('='*40)
saque = int(input('Qual o valor você quer sacar? R$'))
# Abaixo a minha solução... Mas vou fazer a do Guanabara
'''cinquenta = saque//50
                        restante = saque%50
                        vinte = restante//20
                        restante = restante%20
                        dez = restante//10
                        restante = restante%10
                        um = restante
                        print(f'Total de {cinquenta} cédulas de R$50')
                        print(f'Total de {vinte} cédulas de R$20')
                        print(f'Total de {dez} cédulas de R$10')
                        print(f'Total de {um} cédulas de R$1')'''
cedula = 50
totced = 0
while True:
    if saque >= cedula:
        saque -= cedula
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totced = 0
        if saque == 0:
            break
print('VOLTE SEMPRE!')



