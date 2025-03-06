cadastro = {'nome': str(input('Nome: ')), 'media': float(input('Média: '))}
print(f'Nome é igual a {cadastro['nome']}'
        f'\nMédia é igual a {cadastro['media']}'
        f'\nSituação é igual a ', end='')
if cadastro['media'] >= 7:
    print('APROVADO!')
else:
    print('REPROVADO!')