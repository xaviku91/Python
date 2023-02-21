### Manejo de ficheros - File Handling ###

# .txt file

# 1. Abrir el fichero
# Leer y escribir en el fichero
abrir_fichero = open("Aprendizaje/Mouredev/mi_fichero.txt", "r+")
#print(abrir_fichero.read()) #Lee todo el fichero
print(abrir_fichero.read(10)) #Lee los primeros 5 caracteres
print(abrir_fichero.readline()) #Lee la primera línea
print(abrir_fichero.readline()) #Lee la siguiente línea
print(abrir_fichero.readlines()) #Lee todas las líneas y las devuelve en una lista
for line in abrir_fichero.readlines(): #Llamamos a readlines y las junta a un listado y lo recorremos con un for y las lee linea a linea a linea y las imprime
    print(line)

#2. Escribir en el fichero
abrir_fichero.write("\nMi ciudad es Sabadell") #Escribe en el fichero con un salto de linea y lo guarda en el fichero