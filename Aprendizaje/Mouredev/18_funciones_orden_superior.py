### Funciones de orden superior ###
# Una función de orden superior es una función que recibe como parámetro otra función o devuelve una función como resultado.
# Las funciones de orden superior son muy útiles para abstraer comportamientos y reutilizar código.


# Función que recibe como parámetro otra función 
def suma_uno(valor):
  return valor + 1

def suma_dos_numeros_y_uno(valor_uno, valor_dos):
  return suma_uno(valor_uno + valor_dos)

print(suma_dos_numeros_y_uno(1, 2))


# Función que devuelve una función como resultado 
def suma_uno(num):
  return num + 1

def suma_cinco(num):
  return num + 5

def suma_dos_numeros_y_uno(num_uno, num_dos, funcion_num):
  return funcion_num(num_uno + num_dos)

print(suma_dos_numeros_y_uno(2, 3, suma_uno))
print(suma_dos_numeros_y_uno(2, 3, suma_cinco))


### Closures ###
# Un closure es una función que recuerda el estado de las variables no locales cuando se crea. Esto quiere decir que una función definida en el ámbito local de otra función recuerda el ámbito en el que se ha creado.

def suma_diez(valor_original):
  def suma(num):
    return num + 10 + valor_original
  return suma

add_closure = suma_diez(1)
print(add_closure(5)) # 16 (5 + 10 + 1)

# Otra manera de hacer lo mismo:
print((suma_diez(1))(5)) # 16 (5 + 10 + 1)


### Decoradores ###
# Un decorador es una función que recibe como parámetro otra función y devuelve una función. Los decoradores son muy útiles para añadir funcionalidades a otras funciones sin modificarlas.
'''
def decorador(funcion):
  def funcion_decorada():
    print("Hola, soy un decorador")
    funcion()
  return funcion_decorada

@decorador

def saludo():
  print("Hola, soy una función")

saludo()
'''

### Built-in Higher Order Functions ###

numeros = [2, 5, 10, 21, 52]

# Map
# map() es una función que recibe como parámetro otra función y una lista. La función que recibe como parámetro debe recibir un solo parámetro y devolver un valor. map() devuelve un iterador que aplica la función a cada elemento de la lista.

def doble(num):
  return num * 2

map(doble, numeros) 

# Para ver el resultado de la función map() debemos convertir el iterador a una lista:
print(list(map(doble, numeros))) # [4, 10, 20, 42]

# Otra manera de hacer lo mismo pero utilizando una lambda además de lo crear una lista, para definir la función:
print(list(map(lambda number: number * 2, numeros))) # [4, 10, 20, 42]


# Filter:
# filter() es una función que recibe como parámetro otra función y una lista. La función que recibe como parámetro debe recibir un solo parámetro y devolver un valor booleano. filter() devuelve un iterador que aplica la función a cada elemento de la lista y devuelve aquellos elementos que devuelven True.
def filtra_valores_mayores_diez(numeros):
  if numeros > 10:
    return True
  return False

# Para ver el resultado de la función filter() debemos convertir el iterador a una lista:
# En este caso nos devuelve los valores que cumplen la condición de la función,
# los números mayores a diez de la variable "números".
print(list(filter(filtra_valores_mayores_diez, numeros)))

# Para ver el resultado de la función (Es lo mismo que la anterior, pero con lambda)
# filter() utilizando una lambda:
print(list(filter(lambda number: number > 10, numeros)))

# Reduce:
# Acumula el valor y lo suma con el anterior valor de la lista. En este caso: (2 + 5 = 7, 7 + 10 = 17, 17 + 21 = 38, 38 + 52 = 90)
# Los dos últimos valores son las sumas de los anteriores, y hemos pedido que nos los devuelva
from functools import reduce

def suma_dos_valores(primer_valor, segundo_valor):
  print(primer_valor) # primer_valor: 38 (2 + 5 + 10 + 21)
  print(segundo_valor) # segundo_valor: 52 (52)
  return primer_valor + segundo_valor # 38 + 52 = 90

print(reduce(suma_dos_valores, numeros))