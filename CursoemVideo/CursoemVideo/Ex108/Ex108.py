import moeda

preço = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(preço)} é {moeda.moeda(moeda.metade(preço))}')
print(f'O dobro de {moeda.moeda(preço)} é {moeda.moeda(moeda.dobro(preço))}')
print(f'Aumentando o preço em 10%, temos {moeda.moeda(moeda.aumentar(preço, 10))}')
print(f'Diminuindo o preço em 13%, temos {moeda.moeda(moeda.diminuir(preço, 13))}')
