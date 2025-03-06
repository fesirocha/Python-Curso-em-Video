teste = list()
teste.append('Gus')
teste.append(40)
galera = list()
galera.append(teste[:])
print(galera)
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
print('####################')
galera2 = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera2)
print(galera2[2][1])
for p in galera2:
    print(p)
for p in galera2:
    print(p[0])

print('####################')

pessoal = list()
dado = list()
for c in range(0 ,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade')))
    pessoal.append(dado[:])
    dado.clear()
print(pessoal)
for p in pessoal:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
    else:
        print(f'{p[0]} é menor de idade')

