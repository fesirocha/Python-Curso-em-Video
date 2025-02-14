# IMC
peso = float(input('Qual seu peso (kg): '))
altura = float(input('Qual sua altura (m): '))
imc = peso/(altura**2)

if imc < 18.5:
    print('IMC: {:.2f} - Você está abaixo do peso (IMC < 18,5)'.format(imc))
elif imc < 25:
    print('IMC: {:.2f} - Você está no peso ideal (18.5 < IMC < 25)'.format(imc))
elif imc < 30:
    print('IMC: {:.2f} - Você está com sobrepeso (25 < IMC < 30)'.format(imc))
elif imc < 40:
    print('IMC: {:.2f} - Você está com obesidade (30 < IMC < 40)'.format(imc))
else:
    print('IMC: {:.2f} - Você está com obesidade mórbida (IMC > 40)'.format(imc))


