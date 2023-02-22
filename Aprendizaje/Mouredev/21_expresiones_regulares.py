### Expresiones regulares ###
# Expresiones regulares son una secuencia de caracteres que forma un patrón de búsqueda

# Se importa el módulo re  (Regular Expressions) para poder utilizar las expresiones regulares
import re

# Se crea una variable con el texto a buscar
texto = "Hola Mundo"

# Se crea una variable con la expresión regular
expresion_regular = "Hola"

# Se crea una variable con la función search() que busca la expresión regular en el texto
resultado = re.search(expresion_regular, texto)

# Se imprime el resultado
print(resultado)

# Se imprime el tipo de dato
print(type(resultado))

# Se imprime el valor de la variable resultado
print(resultado.group())

# Se crea una variable con la función match() que busca la expresión regular al principio del texto
resultado = re.match(expresion_regular, texto)

# Se imprime el resultado
print(resultado)