#Cadastro
maior = homem = mulher = 0
while True:
    print('='*40)
    print(f'{'CADASTRO DE PESSOAS':^40}')
    print('='*40)
    idade = int(input('Idade: '))
    if idade >= 18:
        maior += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if sexo in 'Mm':
        homem += 1
    elif sexo in 'Ff' and idade < 20 :
        mulher += 1
# Perguntar sobre continuar
    op = ' '
    print('-'*40)
    while op not in 'SN':
        op = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if op == 'N':
        break
# Saída
print('='*5, 'FIM DO PROGRAMA', '='*5)
print(f'Total de pessoas com + de 18 anos: {maior}')
print(f'Ao todo temos {homem} homens cadastrados')
print(f'Temos {mulher} mulher(es) com menos de 20 anos')
