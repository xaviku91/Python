### Módulos - modules ###
# Un modulo es un archivo de python que contiene funciones, clases, variables, etc.
import modulo

# Importar todas las funciones del modulo
modulo.sumaValores(1, 2, 3)
# sumaValores(1, 2, 3) # Error porque no se ha importado la función

# Importar solo una función
from modulo import restaValores
restaValores(5, 2, 1)

# importar módulos predefinidos de python
import math 
print(math.pi) # muestra el valor de pi
print(math.pow(2, 3)) # muestra el valor de 2 elevado a 3

# También podemos crear alias
from math import pi as PI_valor
print(PI_valor)
#print(pi) # Error porque se cambió el nombre de la función "pi"