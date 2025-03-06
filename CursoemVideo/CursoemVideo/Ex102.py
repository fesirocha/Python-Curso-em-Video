def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um nº
    :parâmetro num: O número a ser calculado
    :parâmetro show (opcional): mostrar ou não a conta
    :return: retorna o valor do fatorial de num
    """
    f = 1
    for c in range (num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(f' x ', end='')
            else:
                print(f' = ', end='')
        f *= c
    return f

print(fatorial(5, show=True))
