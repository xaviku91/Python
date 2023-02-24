### Expresiones regulares ###
# Expresiones regulares son una secuencia de caracteres que forma un patrón de búsqueda

# Se importa el módulo re  (Regular Expressions) para poder utilizar las expresiones regulares
import re

# Se crea una variable con el texto a buscar
mi_string = "Esta es otra Lección de Python: Es una lección de programación, la número 1."
mi_otro_string = "Esta no es una lección de Java."

variable_match = re.match("Esta es otra", mi_string, re.I) #Guarda el objeto de tipo match en una variable

# re.match: busca la cadena en el texto y devuelve el primer valor encontrado
# re.I: es para que no sea sensible a mayúsculas y minúsculas

'''
print(variable_match) #Muestra el objeto de tipo match
print(variable_match.span()) #Muestra en que posición se encuentra la cadena en el texto
print(variable_match.string) #Muestra el texto completo
print(variable_match.group()) #Muestra la cadena encontrada

inicio, final = variable_match.span() #Guarda en dos variables el inicio y el final de la cadena encontrada
print(mi_string[inicio:final]) # Accede a la variable mi_string y muestra la cadena encontrada desde el inicio hasta el final
'''

'''
print(re.match("Esta es otra", mi_string)) #Muestra "Esta es otra" porque encuentra la cadena en el texto.
print(re.match("otra lección de Python", mi_string, )) #Muestra None porque no funciona con el final de la cadena.
print(re.match("Esta es otra", mi_otro_string)) #Muestra None porque no encuentra la cadena en el texto.
'''

# Comprobamos si la cadena se encuentra en el texto
'''
# Si encuentra el valor:
variable_match = re.match("Esta no es una lección", mi_otro_string, re.I)

# No encuentra el valor:
#variable_match = re.match("Esta es otra lección", mi_otro_string, re.I)


if (variable_match == None): #Si no encuentra la cadena en el texto, muestra el mensaje antes del error
    #También se puede hacer con: if variable_match != None:
    print("No se ha encontrado la cadena en el texto")
    print(variable_match)
    inicio, final = variable_match.span()
    print(mi_otro_string[inicio:final])
else:
    print("Si se ha encontrado la cadena en el texto")
    print(variable_match)
    inicio, final = variable_match.span()
    print(mi_otro_string[inicio:final])
'''

# Search
# Busca la cadena en el texto y devuelve el primer valor encontrado
'''
variable_search = re.search("lección", mi_string, re.I) #Busca la cadena en el texto y devuelve el primer valor encontrado
print(variable_search)
inicio, final = variable_search.span()
print(mi_string[inicio:final])
'''

# Findall
# Busca todas las coincidencias de la cadena en el texto y devuelve una lista con todas las coincidencias
'''
variable_findall = re.findall("lección", mi_string, re.I) #Busca todas las coincidencias de la cadena en el texto y devuelve una lista (array) con todas las coincidencias
print(variable_findall)
'''
# Búsqueda de caracteres [a-c]
# Busca todas las coincidencias de la cadena en el texto y devuelve una lista (array) con todas las coincidencias
'''
variable_findall = re.findall("[a-c]", mi_string, re.I) 
print(variable_findall)

# [^a-c]
# Quita los caracteres que se encuentran entre corchetes y no los muestra, además el resto de caracteres los muestra en una lista (array)
variable_findall = re.findall("[^a-c]", mi_string, re.I)
print(variable_findall)

# [a-zA-Z]
# Muestra los caracteres que se encuentran entre corchetes y los muestra en una lista (array) independientemente de si son mayúsculas o minúsculas
# Pero ignora los números, los espacios y los signos como el punto, la coma o los acentos
variable_findall = re.findall("[a-zA-Z]", mi_string, re.I)
print(variable_findall)

# [0-9]
# Muestra los números que se encuentran entre corchetes y los muestra en una lista (array)
variable_findall = re.findall("[0-9]", mi_string, re.I)
print(variable_findall)

# [0-9a-zA-Z]
# Muestra los números y las letras que se encuentran entre corchetes y los muestra en una lista (array)
variable_findall = re.findall("[0-9a-zA-Z]", mi_string, re.I)
print(variable_findall)

# [0-9a-zA-Z\s]
# Muestra los números, las letras y los espacios que se encuentran entre corchetes y los muestra en una lista (array)
variable_findall = re.findall("[0-9a-zA-Z\s]", mi_string, re.I)
print(variable_findall)

# [0-9a-zA-Z\s\.\,]
# Muestra los números, las letras, los espacios y los signos de puntuación que se encuentran entre corchetes y los muestra en una lista (array)
variable_findall = re.findall("[0-9a-zA-Z\s\.\,]", mi_string, re.I)
print(variable_findall)
'''

# Split
# Separa el texto de una lista (array) cada vez que encuentra el carácter indicado (en este caso ":")
'''
print(re.split(":", mi_string))
'''

# Sub
'''
# Reemplaza todas las coincidencias de la cadena en el texto
print(re.sub("lección", "LECCIÓN", mi_string)) 

# Si queremos reemplazar todas las coincidencias independientemente de si son mayúsculas o minúsculas, añadimos las palabras separadas por "|"
print(re.sub("lección|Lección", "LECCIÓN", mi_string))
# También se puede hacer así: ("[lL]ección", "LECCIÓN", mi_string]")

# Reemplaza solo la primera palabra "lección" por la palabra "curso" en el texto
print(re.sub("lección", "LECCIÓN", mi_string, 1))
'''

# Patrones - Patterns
# Crea un patrón para buscar una cadena en el texto
# Lo mismo que hacemos con la función "sub" pero en este caso lo guardamos en una variable, y parecido a lo que hacemos con la función "findall"
# Pero utilizando la palabra reservada r"".
'''
variable_patron = r"[lL]ección" #Guarda el patrón en una variable
print(re.findall(variable_patron, mi_string)) #Busca la cadena en el texto y devuelve una lista (array) con todas las coincidencias

# Si queremos buscar varias palabras, las separamos con "|"
variable_patron = r"[lL]ección|programación" 
print(re.findall(variable_patron, mi_string))

# Busca las palabras de la a a la z, tanto mayúsculas como minúsculas
variable_patron = r"[a-zA-Z]"
print(re.findall(variable_patron, mi_string))

# También podemos utilizar el search para buscar el patrón en el texto
variable_patron = r"[0-9]"
print(re.findall(variable_patron, mi_string)) # Nos devuelve una lista (array) con los números del 0 al 9 que se encuentran en el texto
print(re.search(variable_patron, mi_string)) #Busca el número y nos proporciona la posición en la que se encuentra

#Busca todo lo que no sean números
variable_patron = r"\D" 
print(re.findall(variable_patron, mi_string))

#Busca todo lo que sean números
variable_patron = r"\d" 
print(re.findall(variable_patron, mi_string))

#Busca los espacios
variable_patron = r"\s" 
print(re.findall(variable_patron, mi_string))

#Busca todo lo que no sean espacios
variable_patron = r"\S" 
print(re.findall(variable_patron, mi_string))

#Busca todo lo que sean letras, números y guiones bajos
variable_patron = r"\w" 
print(re.findall(variable_patron, mi_string))

#Busca en este ejemplo las palabras que contengan la letra "l" ya sea mayúscula o minúscula
variable_patron = r"[lL]\w{1,}"
print(re.findall(variable_patron, mi_string))
'''
'''
email = "xaviku@xaviku.com"
variable_patron = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
print(re.match(variable_patron, email))
print(re.search(variable_patron, email))
print(re.findall(variable_patron, email))

#Retorna una lista vacía porque no encuentra ninguna coincidencia	
email = "xaviku@xaviku"
email = "xaviku@xaviku."
email = "xavikuxaviku.com"
print(re.findall(variable_patron, email))
'''

# Ejemplo del anterior: validador de email (Email validator)
# Pero solo para un email que termine en .com, .es, .org, y solo puedes poner uno de ellos.

import re

email = input("Introduce tu email: ")

variable_patron = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.(com|es|org)$"

if re.match(variable_patron, email):
    print("Email correcto")
else:
    print("Email incorrecto")