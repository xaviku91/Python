### Excepciones básicas - Exception Handing ###

numeroUno = 5
numeroDos = "1"

# El siguiente error se produce porque no se puede sumar un entero con un string
"""
if numeroUno > 3:
  print(numeroUno + numeroDos)
else:
  print("No se cumple la condición")
"""

# Para evitar que el programa se detenga, se puede utilizar un bloque try-except
try:
  print(numeroUno + numeroDos)
except:
  print("No se puede sumar un entero con un string")
  
# Otra forma de solucionar el problema es convertir el string a entero, aunque esto no es la mejor solución
if numeroUno > 3:
  print(numeroUno + int(numeroDos))
else:
  print("No se cumple la condición")



# Try except else finally
# numeroDos = 1 
try:
  print(numeroUno + numeroDos)
  print("Todo salió bien")
except: # Esto se ejecuta si se produce una excepción
  print("Se produjo un error")
  
else: # Esto se ejecuta si no se produce un error
  print("La ejecución continua correctamente") 
finally:# Esto se ejecuta siempre
  print("Continua la ejecución del programa")

# Except con typeError y ValueError
try:
  print(numeroUno + numeroDos)
except TypeError:
  print("Se ha producido un TypeError")
except ValueError:
  print("Se ha producido un ValueError")
  

# Obtener la información del error de la excepción
try:
  print(numeroUno + numeroDos)
except ValueError as errorValue:
  print(errorValue)
except TypeError as errorType:
  print(errorType)
except Exception as errorException:
  print("Se ha producido un error")
  print(errorException)