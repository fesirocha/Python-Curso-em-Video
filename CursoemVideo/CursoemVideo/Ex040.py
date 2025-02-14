# MÉDIA ARITMÉTICA
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
if m < 5:
    print('ALUNO REPROVADO, MÉDIA DE {:.1f}'.format(m))
elif 5 <= m < 7:
    print('ALUNO EM RECUPERAÇÃO, MÉDIA DE {:.1f}'.format(m))
elif m >= 7:
    print('ALUNO APROVADO, MÉDIA DE {:.1f}'.format(m))