#Maior de idade
s = 0
for c in range (0 ,7):
    ano = int(input('Digite o ano de nascimento: '))
    if  ano <= (2025 - 21):
        s += 1
print('{} pessoas são maiores de 21 anos'.format(s))
