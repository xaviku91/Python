### Resolución de ejercicios ###

#0: EL FAMOSO "FIZZ BUZZ”
'''
Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de 5 por la palabra "buzz".
- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
'''


def fizzbuzz():
    for i in range(1,101):
        if i%3==0 and i%5==0:
            print("fizzbuzz")
        elif i%3==0:
            print("fizz")
        elif i%5==0:
            print("buzz")
        else:
            print(i)

fizzbuzz()


#1: ¿ES UN ANAGRAMA?
'''
Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
Un Anagrama consiste en formar una palabra reordenando TODAS
las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.
'''
'''
# Un Anagrama es una palabra igual pero del revés
def es_anagrama(palabra_uno, palabra_dos):
  if palabra_uno.lower() == palabra_dos.lower(): # Si ambas palabras son iguales nos da error, pues no sería un anagrama.
    return False
  return sorted(palabra_uno.lower()) == sorted(palabra_dos.lower())
  # Sorted ordena las palabras en el mismo orden.
  # Lower vuelve todas las palabras en minúsculas
print(es_anagrama("Amor", "Roma"))
'''

#2: LA SUCESIÓN DE FIBONACCI
'''
Escribe un programa que imprima los 50 primeros números de la sucesión
de Fibonacci empezando en 0.
- La serie Fibonacci se compone por una sucesión de números en
la que el siguiente siempre es la suma de los dos anteriores.
0, 1, 1, 2, 3, 5, 8, 13...
'''

def fibonacci():
  
  anterior = 0
  siguiente = 1
  
  for i in range(0,50):
    
    print(anterior)
    
    fibo = anterior + siguiente
    anterior = siguiente
    siguiente = fibo

fibonacci()

# Otra manera de hacer el mismo ejercicio más simplificado
'''
def fibonacci():
  a, b = 0, 1
  for i in range(50):
    print(a)
    a, b = b, a + b

fibonacci()
'''

#3: ¿ES UN NÚMERO PRIMO?
# Un número primo es aquel que solo es divisible por 1 y por sí mismo.
'''
Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.
'''
# Manera de realizar el ejercicio con dos funciones
# La función para comprobar si es primo o no
'''
def es_primo(numero):
  if numero < 2:
    
    return False
  for i in range(2, numero):
    if numero % i == 0:
      return False
    
  return True

# La función para imprimir los números primos entre 1 y 100
def primos():
  for i in range(1, 101):
    if es_primo(i):
      print(i)
      
primos()
'''

# Otra manera de hacer el mismo ejercicio más simplificado.
'''
def es_primo(numero):
  
  for numero in range(1, 101):
    if numero >= 2:
      es_divisible = False
      for i in range(2, numero):
        if numero % i == 0:
          es_divisible = True
          break
      if not es_divisible:
        print(numero)

es_primo()
'''

# La manera más simplificada de hacer el mismo ejercicio
'''
def es_primo(numero):
  for numero in range(1, 101):
    if numero >= 2:
      for i in range(2, numero):
        if numero % i == 0:
          break
      else:
        print(numero)

es_primo()
'''

# Pedir al usuario que introduzca un número y decirle si es primo o no
'''
numero = int(input("Introduce un número para ver si es primo o no: "))

def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero//2+1):
        if numero % i == 0:
            return False
    return True

if es_primo(numero):
    print(f"{numero} es primo")
else:
    print(f"{numero} no es primo")
'''