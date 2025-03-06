#Dicionários
pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade' : 22}
print(pessoas)
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
print('-='*20)
for k, v in pessoas.items():
    print(f'{k} = {v}')
print('-=' * 20)
del pessoas['sexo']
for k, v in pessoas.items():
    print(f'{k} = {v}')
print('-=' * 20)
#Adicionando um valor novo e uma key nova
pessoas['peso'] = 98.5
for k, v in pessoas.items():
    print(f'{k} = {v}')
print('-=' * 40)
print('-=' * 40)
##############
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0]['uf'])
print('-=' * 40)
print('-=' * 40)
###########
estado = dict()
pais = list()
for c in range (0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    pais.append(estado.copy())
for e in pais:
    for v in e.values():
        print(f'{v}/', end='')
    print()




