### Loops - Bucles - ### 

# Bucle while (Se repite mientras la condición se cumpla)
mi_condicion = 0

# Cuando la condición valga 10, el bucle se detiene
# Esto imprime los números del 0 al 9
while mi_condicion < 10:
    print(mi_condicion)
    mi_condicion += 1 # Esto es igual a mi_condicion = mi_condicion + 1

print("Fin del primer bucle while")

mi_nueva_condicion = 0

while mi_nueva_condicion < 10:
    print(mi_nueva_condicion)
    mi_nueva_condicion += 2 
else: # Else es opcional, y no se puede poner if ni else if.
    print("Mi condición ya no es menor que 10")
print("Fin del segundo bucle while")

# Bucle while con break
while mi_condicion < 20:
    print(mi_condicion)
    mi_condicion += 1
    if mi_condicion == 15: 
        print("Mi condición es 15 y sale")
        break # Cuando llega a 15, sale del bucle sin necesidad de que la condición sea mayor que 20
print("Fin del tercer bucle while")

# Bucle while con continue
while mi_condicion < 30:
    print(mi_condicion)
    mi_condicion += 5
    if mi_condicion == 25: 
        print("Mi condición es 25 y continua")
        continue # Cuando llega a 25 imprime y después continua con el bucle hasta llegar a 30
print("Fin del cuarto bucle while")

# Bucle for (Se repite tantas veces como elementos tenga la lista)
mi_lista = [31, 24, 56, 78, 100]

print("Lista")
for elemento in mi_lista:
    print(elemento) # Imprime los elementos de la lista en orden

# Bucle for con break
for elemento in mi_lista:
    print(elemento)
    if elemento == 56:
        print("Elemento 56 y sale")
        break # Cuando llega a 56, sale del bucle sin necesidad de que se impriman todos los elementos de la lista que vendrían después
      
# Bucle for con continue
for elemento in mi_lista:
    print(elemento)
    if elemento == 56:
        print("Elemento 56 y continua")
        continue # Cuando llega a 56 imprime y después continua con el bucle hasta llegar a 100

# Bucle for con range
for elemento in range(10): # Imprime los números del 0 al 9
    print(elemento)

print("Tupla")
mi_tupla = (31, 1.64, "Xavi", "Sabadell", 100)
for elemento in mi_tupla:
    print(elemento) # Imprime los elementos de la tupla en orden

print("Set")
mi_set = {"Xavi", "Sabadell", 78, 100}
for elemento in mi_set:
    print(elemento) # Imprime los elementos del set en orden aleatorio
    
print("Diccionario . Claves")
mi_dict = {"nombre": "Juan", "apellido": "Pérez", "edad": 25}
for elemento in mi_dict:
    print(elemento) # Imprime las claves del diccionario

print("Diccionario - solo valores")
for elemento in mi_dict.values():
    print(elemento) # Imprime los valores del diccionario

print("Diccionario - claves y valores")
for clave, valor in mi_dict.items():
    print(clave, valor) # Imprime las claves y los valores del diccionario

# Bucle for con else
for elemento in mi_dict:
    print(elemento)
else:
    print("Fin del bucle for")

# Bucle for con break
for elemento in mi_dict:
    print(elemento)
    if elemento == "edad":
        print("Edad y sale")
        break # Cuando llega a edad, sale del bucle sin necesidad de que se impriman las claves que vendrían después