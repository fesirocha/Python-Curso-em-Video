import math
ang=float(input("Digite um angulo:"))
ang=math.radians(ang)

print("O seno desse angulo é {:.2f}, cosseno é {:.2f} e tangente é {:.2f}".format(math.sin(ang), math.cos(ang), math.tan(ang)))
