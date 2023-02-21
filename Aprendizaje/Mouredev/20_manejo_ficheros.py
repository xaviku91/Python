### Manejo de ficheros - File Handling ###

import json
import os

# 1. .txt file

# Abrir el fichero
# Primero buscará el fichero en la carpeta donde se encuentra el script
txt_file = open("Aprendizaje/Mouredev/mi_fichero.txt", "r+")

# Al no encontrarlo, creará el fichero.
txt_file.write("Mi nombre es Xavi\nMi apellido es Quesada\nTengo 31 años\nY mi lenguaje favorito es Python")

# Leer el fichero
#print(txt_file.read()) #Lee todo el fichero
print(txt_file.read(10)) #Lee los primeros 10 caracteres
print(txt_file.readline()) #Lee la primera línea
print(txt_file.readline()) #Lee la siguiente línea
print(txt_file.readlines()) #Lee todas las líneas y las devuelve en una lista

for line in txt_file.readlines(): #Llamamos a readlines y las junta a un listado y lo recorremos con un for y las lee linea a linea a linea y las imprime
    print(line)

# Escribe en el fichero con un salto de linea y lo guarda en el fichero
txt_file.write("\nSoy de Sabadell")
print(txt_file.readline()) # Lee la línea añadida

# Cierra el fichero
txt_file.close()

with open("Aprendizaje/Mouredev/mi_fichero.txt", "a") as mi_documento: #Con with no hace falta cerrar el fichero
    mi_documento.write("\nTambién me gusta Java") #No se puede escribir en un fichero que se ha abierto con with

# Elimina el fichero
# os.remove("Aprendizaje/Mouredev/mi_fichero.txt")

# 2. .json file
# Json es un formato de datos que se utiliza para intercambiar información entre sistemas

# Crea un fichero json
json_file = open("Aprendizaje/Mouredev/mi_fichero.json", "w+")

# Se crea como un diccionario
json_test = {
    "nombre": "Xavi",
    "apellido": "Quesada",
    "edad": 31,
    "lenguajes": ["Python", "Java", "C++"],
    "ciudad": "Sabadell"
}

# Escribe el diccionario en el fichero
json.dump(json_test, json_file, indent=2) #indent=2 es para que se vea mejor el json haciendo un salto de linea

json_file.close() #Cierra el fichero

# Lee el fichero json
with open("Aprendizaje/Mouredev/mi_fichero.json") as json_file:
    for line in json_file.readlines():
        print(line)

json_dict = json.load(open("Aprendizaje/Mouredev/mi_fichero.json")) #Carga el fichero json y lo convierte en un diccionario
print(json_dict) # Para ver el diccionario
print(type(json_dict)) # Para ver el tipo de dato en este caso es un diccionario
print(json_dict["nombre"]) # Para acceder a un valor del diccionario
