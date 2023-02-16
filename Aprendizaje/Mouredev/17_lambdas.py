### Lambdas ###
# Las lambdas son funciones anónimas, es decir, funciones sin nombre.
# Se utilizan para crear funciones de una sola línea.
# Y se utilizan para crear funciones que se van a utilizar una sola vez.

# Ejemplo de una función lambda que suma, resta, multiplica y divide dos valores:
# Pedimos al usuario que introduzca dos valores y los sumamos:

primer_valor = int(input("Introduce un valor: "))
segundo_valor = int(input("Introduce un valor: "))
valor_uno = int(input("Introduce el valor de suma de función: "))

suma_dos_valores = lambda primer_valor, segundo_valor: primer_valor + segundo_valor
resta_dos_valores = lambda primer_valor, segundo_valor: primer_valor - segundo_valor
multi_dos_valores = lambda primer_valor, segundo_valor: primer_valor * segundo_valor
div_dos_valores = lambda primer_valor, segundo_valor: primer_valor / segundo_valor

print("La suma de los dos valores son: ", suma_dos_valores(primer_valor, segundo_valor))
print("La resta de los dos valores son: ", resta_dos_valores(primer_valor, segundo_valor))
print("La multiplicación de los dos valores son: ", multi_dos_valores(primer_valor, segundo_valor))
print("La división de los dos valores son: ", div_dos_valores(primer_valor, segundo_valor))

# Lambda dentro de una función:
def funcion_lambda(valor_uno):
    return lambda primer_valor, segundo_valor: primer_valor + segundo_valor + valor_uno

print("El resultado de la función lambda es: ", funcion_lambda(valor_uno)(primer_valor, segundo_valor))

# Lambda dentro de una función con condicional:
def funcion_lambda_condicional(valor_uno):
    return lambda primer_valor, segundo_valor: primer_valor + segundo_valor + valor_uno if valor_uno > 10 else primer_valor + segundo_valor - valor_uno # Si el "valor_uno" es mayor que 10, se suma, si no, se resta ambas acciones a primer_valor y segundo_valor.

print("El resultado de la función lambda con condicional es: ", funcion_lambda_condicional(valor_uno)(primer_valor, segundo_valor))