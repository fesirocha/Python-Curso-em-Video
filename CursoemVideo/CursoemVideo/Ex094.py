cadastro = dict()
pessoas = list()
op = ''
sumidade = 0
while True:
    cadastro.clear()
#Cadastro do nome
    cadastro['Nome'] = str(input('Nome: '))
#Cadastro do sexo
    sex = str(input('Sexo [M/F]: ')).strip().upper()[0]
    while sex not in 'FM':
        sex = str(input(f'ERRO! Por favor, digite apenas M ou F: ')).strip().upper()[0]
    cadastro['Sexo'] = sex
#Cadastro da idade
    idade = int(input('Idade: '))
    sumidade += idade
    cadastro['Idade'] = idade
#Incluir dict na list
    pessoas.append(cadastro.copy())
#Questiona se quer continuar
    op = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    while op not in 'SN':
        op = str(input('ERRO! Por favor, digite apenas S ou N: ')).strip().upper()[0]
    if op == 'N':
        break
#Resposta A
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas')
#Resposta B
media = sumidade/len(pessoas)
print(f'B) A média de idade é de {media:.2f} anos')
#Reposta C
print(f'C) As mulheres cadastradas foram: ', end='')
for p in pessoas:
    if p["Sexo"] in 'F':
        print(f'{p["Nome"]} ', end='')
#Resposta D
print(f'\nLista das pessoas que estão acima da média:')
for p in pessoas:
    if p['Idade'] >= media:
        print(f'    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('ENCERRADO')






