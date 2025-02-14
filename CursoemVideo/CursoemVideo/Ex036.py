# EMPRÉSTIMO BANCÁRIO PARA CASA
casa = float(input('Digite o valor (R$) da casa a ser negociada: '))
salario = float(input('Digite o seu salário (R$) mensal: '))
anos = int(input('Digite em quantos anos deseja quitar o valor da casa: '))
parcela = (casa/(anos*12))
if parcela > (salario*0.3):
    print('EMPRÉSTIMO NEGADO, POIS VALOR DA PARCELA ULTRAPASSA 30% DO SALÁRIO MENSAL')
else:
    print('EMPRÉSTIMO APROVADO. SERÃO AO TODO {} PARCELAS DE R${:.2f}'.format(anos*12, parcela))