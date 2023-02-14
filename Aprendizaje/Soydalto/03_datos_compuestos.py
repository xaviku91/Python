### Datos compuestos ###

# Listas (se pueden modificar)
lista = ["Xavi", "Sabadell", True, 1.64, 31]
print(lista)

# Muestra el tipo de dato
print(type(lista))

# Muestra el primer elemento de la lista
print(lista[0])

# Muestra el último elemento de la lista
print(lista[4])
print(lista[-1]) # También se puede hacer así si no sabemos el número de elementos que tiene la lista

lista[0] = "Pedro" # Modifica el primer elemento de la lista
print(lista) # Muestra la lista modificada

# Tuplas (no se pueden modificar)
tupla = ("Xavi", "Sabadell", True, 1.64, 31)
#tupla[0] = "Pedro" # Da error porque no se puede modificar

# Sets (no se pueden modificar, no se pueden repetir elementos) No tiene un orden.
mi_set = {"Xavi", "Sabadell", True, 1.64, 31, "Xavi"}
#mi_set[0] = "Pedro" # Da error porque no se puede modificar
print(mi_set) # Muestra el set sin repetir elementos, en este caso "Xavi" solo aparece una vez

#print(mi_set[0]) # Da error porque no se puede acceder a un elemento de un set por su posición

# Diccionarios (se pueden modificar)
diccionario = {
  "nombre": "Xavi", 
  "ciudad": "Sabadell", 
  "edad": 31
}

print(diccionario) # Muestra el diccionario
print(diccionario["nombre"]) # Muestra el valor de la clave "nombre"

#print(diccionario[2]) # Da error porque no se puede acceder a un elemento de un diccionario por su posición

# Muestra todas las claves del diccionario
print(diccionario.keys())

# Muestra todos los valores del diccionario
print(diccionario.values())

# Muestra todas las claves y valores del diccionario
print(diccionario.items())

# Muestra el número de elementos del diccionario
print(len(diccionario))

# Añade un elemento al diccionario
diccionario["altura"] = 1.64
print(diccionario)

# Modifica un elemento del diccionario
diccionario["nombre"] = "Pedro"
print(diccionario)

# Elimina un elemento del diccionario
del diccionario["altura"]
print(diccionario)

# Elimina el diccionario
'''print(diccionario.clear())
print(diccionario) # Muestra el diccionario vacío "{}" none
print(len(diccionario)) # Muestra el número de elementos del diccionario (0)
'''

'''
# Elimina el diccionario
#del diccionario
#print(diccionario) # Da error porque el diccionario ya no existe'''

# Copia un diccionario
diccionario2 = diccionario.copy()
print(diccionario2)

# Unir dos diccionarios
diccionario3 = {**diccionario2, **diccionario}

print("Este es el diccionario 3: ",diccionario3)