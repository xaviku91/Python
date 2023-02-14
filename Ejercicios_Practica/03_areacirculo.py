#Calcular el área de un círculo, donde el usuario ingresa el radio.

import math

radio = float(input("Ingrese el radio del círculo: "))
area = math.pi * (radio ** 2)

print("El área del círculo es: ", area)