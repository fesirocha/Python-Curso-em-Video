def maior(* valores):
    max = cont = 0
    tam = len(valores)
    print('=-'*20)
    print('Analisando os valores passados...')
    for c in valores:
        if cont == 0:
            max = c
        else:
            if c > max:
                max = c
        cont += 1
    print(f'{valores} Foram informados {tam} valores ao todo')
    print(f'O maior valor informado foi {max}')


maior(2, 2, 6, 8, 5)
maior (2, 8)
maior (1)
maior (1, 2, 6, 5, 10, 210)
maior (0)
maior ()