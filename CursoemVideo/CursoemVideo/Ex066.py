#999
n = s = cont = 0
while True:
    n = int(input('Digite um nº: (999 para parar) '))
    if n == 999:
        break
    s += n
    cont += 1
print(f'Foram digitados {cont} números e a soma foi de {s}')