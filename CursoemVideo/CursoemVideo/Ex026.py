frase = str(input("Frase a ser analisada: ").strip().upper())
print("A letra A aparece {} vezes na frase".format(frase.count('A')))
print("A posição do primeiro A é: {}".format(frase.find('A') + 1))
print("A última ocorrência de A é na posição {}".format(frase.rfind('A') + 1))
