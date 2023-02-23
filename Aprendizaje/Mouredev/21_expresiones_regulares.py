### Expresiones regulares ###
# Expresiones regulares son una secuencia de caracteres que forma un patrón de búsqueda

# Se importa el módulo re  (Regular Expressions) para poder utilizar las expresiones regulares
import re

# Se crea una variable con el texto a buscar
mi_string = "Esta es otra lección de Python."
mi_otro_string = "Esta no es una lección de Python."

variable_match = re.match("Esta es otra", mi_string, re.I) #Guarda el objeto de tipo match en una variable

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