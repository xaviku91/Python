### Manejo de paquetes - Package Manager ###
# Es un gestor de paquetes que nos permite instalar paquetes de terceros.

# Pip - https://pypi.org/

# Instalar un paquete
# En terminal
# 1. Poner para saber la versión de pip:
# pip --version

# 2. En caso de no tener pip instalado, instalarlo:
# pip install pip

# 3. Actualizar pip:
# pip install --upgrade pip

# 4. Desinstalar pip:
# pip uninstall pip

# 5. Instalar un paquete:
# pip install nombre_del_paquete

# 6. Desinstalar un paquete:
# pip uninstall nombre_del_paquete


from mypackage import arithmetics
import requests
import pandas
import numpy

# Librería numpy
'''
print(numpy.version.version)

variable_numpy = numpy.array([1, 14, 22, 34])
print(variable_numpy)

print(variable_numpy[2])

print(variable_numpy * 2)
'''

# Librería pandas

# Librería requests
'''
respuesta = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
print(respuesta)
print(respuesta.status_code)
print(respuesta.text)  # Devuelve un string
print(respuesta.json())  # Devuelve un diccionario
'''

# Paquetes
# Creamos un paquete llamado mypackage y utilizamos el fichero arithmetics.py
print(arithmetics.suma_dos_valores(2, 3))

# El __init__.py es un fichero que se ejecuta cuando se importa un paquete
