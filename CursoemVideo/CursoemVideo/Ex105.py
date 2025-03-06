def notas(*n, sit=False):
    """
    Função para analisar notas e situação de vários aluns
    Args:
        *n: Pode ser adicionado uma ou mais notas
        sit: valor opcional, indicando se deve ou não mostrar a situação da turma

    Returns: Retorna um dicionário com várias informações sobre a situação da turma

    """
    boletim = dict()
    boletim['Total de Notas'] = len(n)
    boletim['Maior Nota'] = max(n)
    boletim['Menor Nota'] = min(n)
    boletim['Média'] = sum(n)/len(n)
    if sit:
        if boletim['Média'] >= 7:
            boletim['Situação'] = 'BOA'
        elif boletim['Média'] >= 5:
            boletim['Situação'] = 'RAZOÁVEL'
        else:
            boletim['Situação'] = 'RUIM'
    return boletim

resp = notas(5, 8, 10, 4, 8, sit=True)
print(resp)
help(notas)