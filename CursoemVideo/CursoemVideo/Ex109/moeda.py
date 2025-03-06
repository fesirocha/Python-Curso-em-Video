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

