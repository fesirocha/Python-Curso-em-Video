def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg:.2f}x{comp:.2f} é de {a:.2f}m²')

print(f'{'CONTROLE DE TERRENOS':^40}')
print('-'*40)
area((float(input(f'LARGURA (m): '))),(float(input('COMPRIMENTO (m): '))))
