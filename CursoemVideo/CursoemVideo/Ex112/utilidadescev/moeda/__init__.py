def aumentar(preço=0, porcentagem=0, formato=False):
    ajustado = preço + preço*(porcentagem/100)
    return ajustado if formato is False else moeda(ajustado)

def diminuir(preço = 0, porcentagem = 0, formato=False):
    ajustado = preço - preço*(porcentagem/100)
    return ajustado if formato is False else moeda(ajustado)

def metade(preço = 0, formato=False):
    ajustado = preço/2
    return ajustado if formato is False else moeda(ajustado)

def dobro(preço = 0, formato=False):
    ajustado = preço*2
    return ajustado if formato is False else moeda(ajustado)

def moeda(ajustado = 0, moeda = 'R$'):
    return f'{moeda}{ajustado:6.2f}'.replace('.',',')

def resumo(preço = 0, aumento = 0, diminui = 0):
    print(f'A metade de {moeda(preço)} é {metade(preço, True)}')
    print(f'O dobro de {moeda(preço)} é {dobro(preço, True)}')
    print(f'Aumentando o preço em {aumento}%, temos {aumentar(preço, aumento, True)}')
    print(f'Diminuindo o preço em {diminui}%, temos {diminuir(preço, diminui, True)}')

