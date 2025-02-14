#Sexo M ou F
sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MFmf':
    sexo = str(input('Dados inválidos! Digite novamente. Por favor, informe seu sexo [M/F]: ')).strip().upper()[0]
print('OBRIGADO!')

