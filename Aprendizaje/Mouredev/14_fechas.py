### Fechas - Date ###

# DateTime - Fecha y hora (año, mes, día, hora, minutos, segundos...)
from datetime import datetime

# Imprimir la fecha sin variable
'''
print(datetime.now())
print(datetime.now().year)
print(datetime.now().month)
print(datetime.now().day)
'''

# Imprimir la fecha con variable
'''
ahora = datetime.now()
print(ahora)
print(ahora.year)
print(ahora.month)
print(ahora.day)
print(ahora.hour)
print(ahora.minute)
'''
'''
# Imprimir la fecha con formato
otra_fecha = ahora.timestamp()
print(otra_fecha)
'''

# Funciones con fecha

# Definimos el nombre y formato de la fecha
year_2023 = datetime(2023, 1, 1)

def print_fecha(fecha):
  print(fecha.year)
  print(fecha.month)
  print(fecha.day)
  print(fecha.hour)
  print(fecha.minute)
  print(fecha.timestamp())

print_fecha(year_2023) # Llamamos a la función e imprimirá la fecha con el formato minimo necesario que es el año, mes y día, el resto puede ser 0, además de imprimir el timestamp

# Time - Hora (solo hora, minutos y segundos)
from datetime import time
current_time = time(1, 20, 32)
print(current_time)
print(current_time.hour)
print(current_time.minute)
print(current_time.second)


# Date - Fecha (solo año, mes y día)
from datetime import date
nueva_fecha = date.today()
print(nueva_fecha)

# Podemos definir una fecha concreta
nueva_fecha = date(2023, 1, 1)
print(nueva_fecha)

# Sumar y restar días a una fecha
fecha_suma = date(nueva_fecha.year, nueva_fecha.month, nueva_fecha.day + 5)
print(fecha_suma) # Imprime la fecha con 5 días más
