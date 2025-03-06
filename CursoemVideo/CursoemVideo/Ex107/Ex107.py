import moeda

preço = float(input('Digite o preço: R$ '))
print(f'A metade do preço é {moeda.metade(preço)}')
print(f'O dobro do preço é {moeda.dobro(preço)}')
print(f'Aumentando o preço em 10%, temos {moeda.aumentar(preço, 10)}')
print(f'Diminuindo o preço em 13%, temos {moeda.diminuir(preço, 13)}')
