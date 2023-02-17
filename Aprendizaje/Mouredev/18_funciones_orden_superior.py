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

numeros = [2, 5, 10, 21]

# Map
# map() es una función que recibe como parámetro otra función y una lista. La función que recibe como parámetro debe recibir un solo parámetro y devolver un valor. map() devuelve un iterador que aplica la función a cada elemento de la lista.

def doble(num):
  return num * 2

map(doble, numeros) 
print(list(map(doble, numeros))) # [4, 10, 20, 42]