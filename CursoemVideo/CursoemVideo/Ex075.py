lista = ((int(input('Digite um valor: '))), (int(input('Digite outro valor: '))),
        (int(input('Digite outro valor: '))), (int(input('Digite o último valor: '))))
print(f'O número 9 apareceu {lista.count(9)} vezes')
if 3 in lista:
    print(f'O primeiro valor 3 apareceu na {lista.index(3) + 1}ª posição')
else:
    print('O valor 3 não foi digitado')
print('OS valores pares digitados foram ', end='')
for n in lista:
   if n % 2 == 0:
       print(n, end=' ')
