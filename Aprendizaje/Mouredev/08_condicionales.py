### Condicionales ###

my_condition = False
if my_condition: #Solo se ejecuta cuando es "True"
  #Sería lo mismo que: if my_condition == True:
  print("Se ejecuta la condición del if")
print("La ejecución continúa después del if")

#Comprobar el valor de la condición
my_condition = 3 * 3
if my_condition == 10: 
  print("Se ejecuta la condición del segundo if")
  print("La ejecución continúa después del segundo if")
  
if my_condition >= 10:
      print("Es mayor o igual a 10")
else:     
      print("Es menor que 10")


if my_condition > 10 and my_condition < 20:
      print("Es mayor que 10 y menor que 20")
elif my_condition == 9:
      print("Es igual a 9") #Aunque la condición es menor que 10, en este caso imprime está ya que se ejecuta primero y se cumple dicha condición de que es igual a 9 y ya no ejecuta lo siguiente.
else:     
      print("Es menor o igual a 10 o mayor o igual a 20")
print("La ejecución continúa")

my_string = "Mi cadena de texto"
if my_string:
  print("Mi cadena de texto no está vacía")
if my_string == "Otra cadena de texto":
  print("Esta cadena no se imprime")
  
my_string = ""
if not my_string:
  print("Mi cadena de texto está vacía")