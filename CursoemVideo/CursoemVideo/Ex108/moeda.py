def aumentar(preço = 0, porcentagem = 0):
    preço = preço + preço*(porcentagem/100)
    return preço

def diminuir(preço = 0, porcentagem = 0):
    preço = preço - preço*(porcentagem/100)
    return preço

def metade(preço = 0):
    preço = preço/2
    return preço

def dobro(preço = 0):
    preço = preço*2
    return preço

def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda}{preço:6.2f}'.replace('.',',')

