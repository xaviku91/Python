### Manejo de ficheros - File Handling ###

#1 .txt file

# Abrir el fichero
# Primero buscará el fichero en la carpeta donde se encuentra el script
abrir_fichero = open("Aprendizaje/Mouredev/mi_fichero.txt", "w+")

#Al no encontrarlo, creará el fichero.
abrir_fichero.write("Mi nombre es Xavi\nMi apellido es Quesada\nTengo 31 años\nY mi lenguaje favorito es Python") #Escribe en el fichero con un salto de linea y lo guarda en el fichero

# Leer el fichero
#print(abrir_fichero.read()) #Lee todo el fichero
print(abrir_fichero.read(10)) #Lee los primeros 5 caracteres
print(abrir_fichero.readline()) #Lee la primera línea
print(abrir_fichero.readline()) #Lee la siguiente línea
print(abrir_fichero.readlines()) #Lee todas las líneas y las devuelve en una lista

for line in abrir_fichero.readlines(): #Llamamos a readlines y las junta a un listado y lo recorremos con un for y las lee linea a linea a linea y las imprime
    print(line)

#Escribe en el fichero con un salto de linea y lo guarda en el fichero
abrir_fichero.write("\nSoy de Sabadell") 
print(abrir_fichero.read()) #Lee todo el fichero

#Cierra el fichero
abrir_fichero.close() 

#Elimina el fichero
import os
#os.remove("Aprendizaje/Mouredev/mi_fichero.txt")


# 2. .json file
#  Json es un formato de datos que se utiliza para intercambiar información entre sistemas
import json

# Crea un fichero json
json_file = open("Aprendizaje/Mouredev/mi_fichero.json", "w+")

# Se crea como un diccionario
json_test = {"nombre": "Xavi", "apellido": "Quesada", "edad": 31, "lenguajes": ["Python", "Java", "C++"], "ciudad": "Sabadell"}

#Escribe el diccionario en el fichero
json.dump(json_test, json_file, indent=2) #indent=2 es para que se vea mejor el json haciendo un salto de linea