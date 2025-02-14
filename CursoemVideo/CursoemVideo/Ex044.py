# CÁLCULO PREÇO
valor = float(input('Qual o preço normal do produto? R$'))
print('Digite abaixo o número correspondente a opção de pagamento!')
print(' [1] Dinheiro\n [2] Cheque\n [3] Cartão à vista\n [4] Cartão 2x\n [5] Cartão 3x ou +')
opcao = int(input('Digite a opção selecionada: '))

if (opcao == 1) or (opcao == 2):
    produto = valor * 0.90
    print('O valor do produto será de R${}'.format(produto))
elif opcao == 3:
    produto = valor * 0.95
    print('O valor do produto será de R${}'.format(produto))
elif opcao == 4:
    print('O valor do produto será de R${}'.format(valor))
else:
    produto = valor*1.2
    print('O valor do produto será de R${}'.format(produto))
