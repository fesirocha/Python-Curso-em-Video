salario = float(input('Qual seu salário atual? (Em R$) '))
print ('Seu novo salário será de R${}'.format(salario*1.1) if (salario > 1250) else 'Seu novo salário será de R${}'.format((salario*1.15)))