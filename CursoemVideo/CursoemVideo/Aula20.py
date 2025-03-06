#Funções
def soma(a, b):
    s = a + b
    print(s)
def linha():
    print('-'*30)
def contador(*num):
        tam = len(num)
        print(f'Recebi os valores {num} e são ao todo {tam} números')
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *=2
        pos +=1
def soma2(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')

soma(4,5)
linha()
contador(2, 7, 7)
contador(8,0)
contador(4,4,7,6,0)
linha()
valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)
linha()
soma2(5, 2)
soma2(2,9,4)





