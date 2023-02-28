### Type Hints - Anotaciones de tipo ###

my_string_variable = "My string variable"
print(my_string_variable)

print(type(my_string_variable))

# my_string_variable ha pasado de ser un string a ser un int
my_string_variable = 2
print(my_string_variable)
print(type(my_string_variable))

# Para evitar esto, podemos utilizar Type Hints (Anotaciones de tipo)
# Sirve para indicar el tipo de dato que se espera que tenga una variable
# Se utiliza el símbolo : seguido del tipo de dato que se espera que tenga la variable
my_string_variable: str = "My typed string variable"
print(my_string_variable)
print(type(my_string_variable))
