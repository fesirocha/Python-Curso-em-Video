nome = str(input("Digite seu nome completo: ")).strip().upper()
print("Prazer em te conhecer!")
nomes = nome.split()
print("Seu primeiro nome é {}".format(nomes[0]))
print("Seu último nome é {}".format(nomes[len(nomes) - 1]))