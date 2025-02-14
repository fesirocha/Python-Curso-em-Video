n1=int(input('Digite um numero:'))
n2=int(input('Digite outro numero'))
soma = n1 + n2
div = n1/n2
mult = n1*n2
di = n1//n2
pot = n1**n2

print('A soma deles é {} \n a divisao é {:1} e a multipicação é {}'.format(soma, div, mult), end="...")
print('a divisao inteira é {}\n e a exponenciação é {}'.format(di, pot))

