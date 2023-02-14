#Dolar a euro
print("DOLAR A EURO \n")
precio_dolar = float(input("Ingresa el precio del Euro frente al Dólar "))
dolares = float(input("Ingresa la cantidad total de Dólares: "))
euros = dolares * precio_dolar
print(f"Los {dolares} dólares equivalen a {euros} euros")

print("\n")

print("EURO A DOLAR \n")
#Euro a Dolar
precio_euro = float(input("Ingresa el precio del Dólar frente al Euro "))
euro = float(input("Ingresa la cantidad total de Euros: "))
dolar = euro * precio_euro 
print(f"Los {euro} Euros equivalen a {dolar} Dólares")