# Sintaxis condicionales

# Simple if
if True: 
  print("Es verdadero")

# Simple else
if False:
  print("Es falso")
else:
  print("Es verdadero")

# elif: para else anidados sin code hell

dia = int(input("Ingrese número del dia: "))

if dia == 1:
  print(f"El día {dia} de la semana es Lunes")
elif dia == 2:
  print(f"El día {dia} de la semana es Martes")
elif dia == 3:
  print(f"El día {dia} de la semana es Miércoles")
elif dia == 4:
  print(f"El día {dia} de la semana es Jueves")
elif dia == 5:
  print(f"El día {dia} de la semana es Viernes")
elif dia < 8:
  print(f"El día {dia} es parte del fin de semana")
else:
  print("Día inexistente")

# And | or
pais = "Rusia"

if pais == "Argentina" or pais == "Mexico" or pais == "Uruguay":
  print("Su país es de habla hispana")
else:
  print("Su país no es de habla hispana")

# Ejemplo de arriba negado con not
pais = "Argentina"

if not(pais == "Argentina" or pais == "Mexico" or pais == "Uruguay"):
  print("Su país no es de habla hispana")
else:
  print("Su país es de habla hispana")