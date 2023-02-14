### Listas ###

#Ambos constructores sirven para crear una lista.
mi_lista = list()
mi_otra_lista = []

print(len(mi_lista))

mi_lista = [35, 24, 62, 51, 30, 30, 17]

print(mi_lista)
print(len(mi_lista))

mi_otra_lista = [31, 1.64, "Xavi", "Quesada"]

print(type(mi_lista))
print(type(mi_otra_lista))

#Cuenta la lista de adelante hacia atrás --> .
print(mi_otra_lista[0])
print(mi_otra_lista[1])

#Cuenta la lista de atrás adelante <-- .
print(mi_otra_lista[-1])
print(mi_otra_lista[-3])

#Error lista
#print(mi_otra_lista[5])
#print(mi_otra_lista[-5])

#Contar mismos valores en las listas.
print(mi_otra_lista.count("Quesada"))
print(mi_lista.count(30))

edad, altura, nombre, apellido = mi_otra_lista
print(nombre)

#Concatenar listas
print(mi_lista + mi_otra_lista)

#Convertir lista a string.
#mi_lista = "Hola Python"
#print(mi_lista)
#print(type(mi_lista))

#Elementos en listas
mi_otra_lista.append("Empresa S.L")
print(mi_otra_lista) #Inserta al final el dato

mi_otra_lista.insert(1, "Sabadell")
print(mi_otra_lista) #Inserta en el numero donde propongo.

#Cambiar un valor en una posición en concreto.
mi_otra_lista[1] = "Barcelona"
print(mi_otra_lista)

#copiar lista
mi_nueva_lista = mi_lista.copy()

#Borrar lista
mi_lista.clear()
print(mi_lista) #Se ha borrado
print(mi_nueva_lista) #Esta la lista que habíamos copiado

#Revertir la lista
mi_nueva_lista.reverse()
print(mi_nueva_lista)

#Ordenar lista
mi_nueva_lista.sort()
print(mi_nueva_lista)

#Mostrar partes de la lista
print(mi_nueva_lista[1:4]) #Muestra lo que hay entre el 1 y el 4 pero solo mostraría el 1,2,3 el 4 no

#Remover un valor
#mi_otra_lista.remove("Sabadell")
#print(mi_otra_lista)

#elimina el elemento seleccionado
#mi_lista.remove(30)
#print(mi_lista)

#elimina el ultimo elemento
#mi_lista.pop()
#print(mi_lista)

#elimina el ultimo elemento y lo mueve fuera de la lista
#print(mi_lista.pop())
#print(mi_lista)

#elimina el elemento seleccionado de la lista y lo saca de la lista
#print(mi_lista.pop(1))
#print(mi_lista)

#Eliminar un elemento y guardarlo en un lugar concreto:
#mi_pop = mi_lista.pop(0)
#print(mi_lista)
#print(mi_pop)

#Eliminar un elemento de una lista
#del mi_lista[2]
#print(mi_lista)