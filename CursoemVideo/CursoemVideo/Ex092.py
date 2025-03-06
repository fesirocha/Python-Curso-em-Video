#Cadastro de Funcionários
from datetime import datetime
cadastro = dict()
cadastro['Nome'] = str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
cadastro['Idade'] = (datetime.now().year - nascimento)
cadastro['CTPS'] = int(input('Carteira de Trabalho (0 caso não tenha): '))
if cadastro['CTPS'] != 0:
    cadastro['Ano de Contratação'] = int(input('Ano de contratação: '))
    cadastro['Salário (R$)'] = float(input('Salário: R$'))
    cadastro['Aposentadoria'] = cadastro['Idade'] + (cadastro['Ano de Contratação'] + 35) - datetime.now().year
print('-='*20)
for k, v in cadastro.items():
    print(f'- {k}: {v}')


