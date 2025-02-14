vel = int(input('Qual a velocidade do veículo? (km/h) ')) #Entrada do valor de velocidade
if (vel > 80):
    print ('VOCÊ FOI MULTADO NO VALOR DE R${}'.format((vel - 80)*7)) #Condicional acima do limite de velocidade
else:
    print('Bom dia, dirija com segurança') #Condicional abaixo da velocidade