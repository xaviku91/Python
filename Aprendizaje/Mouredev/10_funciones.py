### Funciones ###

# Función sin parámetros
def mi_funcion():
    print("Esto es una función")

mi_funcion() # Llamada a la función

# Función con parámetros
def suma(a, b):
  print(a + b)

suma(5, 7) # Llamada a la función
suma(230, 4595) 
suma("Hola ", "Mundo") # Concatenación de cadenas
suma(1.3, 2.5) # Suma de números decimales

# Función con parámetros y retorno
def nueva_suma(a, b):
  return a + b # Devuelve el resultado de la suma

print(nueva_suma(5, 7)) # Llamada a la función y muestra el resultado

resultado = nueva_suma(5, 7) # Llamada a la función y asignación del resultado a la variable resultado
print(resultado) # Muestra el resultado de la variable resultado

#
def print_nombre (nombre, apellido):
  print(f"Tu nombre es {nombre} {apellido}")

print_nombre("Juan", "Pérez") # Llamada a la función

#Tambien puedes cambiar los parametros de la función
print_nombre(apellido="Juan", nombre="Pérez")

# Función con parámetro por defecto
def print_nombre_por_defecto(nombre, apellido, alias = "Sin alias"): # El parámetro alias tiene un valor por defecto
  print(f"Tu nombre es {nombre} {apellido} y tu alias es {alias}")
print_nombre_por_defecto("Juan", "Pérez") # Llamada a la función sin el parámetro alias imprime el valor por defecto
print_nombre_por_defecto("Xavi", "Quesada","Xaviku") # Llamada a la función con el parámetro alias imprime el valor asignado

# Función con parámetros variables
def print_texto(*texto):
  print(texto)
print_texto("Hola Mundo", "Python", "Como estás") # Llamada a la función con varios parámetros 

def print_upper_texto(*texto):
  for t in texto:
    print(t.upper())
print_upper_texto("Hola Mundo", "Python", "Como estás") # Llamada a la función y los convierte a mayúsculas por cada uno de los textos introducidos

# Función con parámetros variables y parámetro por defecto
def print_texto_defecto(*texto, alias = "Sin alias"):
  print(f"Alias: {alias}")
  for t in texto:
    print(t)
print_texto_defecto("Hola Mundo", "Python", "Como estás", alias = "Xaviku") # Llamada a la función con varios parámetros y el parámetro alias

# Ver el tipo de dato de los parámetros
def print_ver_tipo(*texto):
  print(type(texto))
  for t in texto:
    print(t.upper())
print_ver_tipo("Hola mundo", "Python", "Como estás") # Además de ver y convertir a mayúsculas los textos, también veremos el tipo de dato de los parámetros