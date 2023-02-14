### Sets ###
mi_set = set()
mi_otro_set = {} #Vacío nos marca diccionario pero si rellenamos se vuelve set nuevamente.

print(type(mi_set))
print(type(mi_otro_set))

mi_otro_set = {"Xavi", "Quesada", 31}
print(type(mi_otro_set))

print(len(mi_otro_set))
#print(mi_otro_set[0]) no se puede acceder 

mi_otro_set.add("Sabadell")
mi_otro_set.add("Sabadell") #Un set no admite repetidos.
print(mi_otro_set) #Un set no es una estructura ordenada.

#Comprobar si un elemento existe en un set
print("Xavi" in mi_otro_set)
print("Xavu" in mi_otro_set)

mi_otro_set.remove("Sabadell")
print(mi_otro_set)

#Reiniciar valores
mi_otro_set.clear()
print(len(mi_otro_set))

#Borrar set
#del mi_otro_set

#Transformar set en lista asi podríamos tenerla ordenada o acceder a un elemento en concreto
mi_set = {"Xavi", "Quesada", 35}
mi_lista = list(mi_set)
print(mi_lista)
print(mi_lista[1])

#Unir sets
mi_otro_set = {"JavaScript", "Python", "HTML"}
mi_nuevo_set = mi_set.union(mi_otro_set)
print(mi_nuevo_set)

#No puedes repetir cosas que ya habían sido añadidas
print(mi_nuevo_set.union(mi_nuevo_set)) #No duplica, porque no acepta duplicados.

#Añadir mas cosas 
print(mi_nuevo_set.union({"CSS"})) #Aquí añadirá CSS al set

#Buscar la diferencia entre distintos sets
print(mi_nuevo_set.difference(mi_set))
print(mi_set.difference(mi_otro_set))