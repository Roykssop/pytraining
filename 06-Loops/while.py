numero = int(input("Ingrese el número de la tabla que desea ver: "))
contador = 0

if numero < 1:
  numero = 1

print(f"######## TABLA DE MULTIPLICAR DEL {numero} ############")

while contador <= 10:
  print(f"El resultado de {numero} x {contador} es = { contador * numero } ")
  contador += 1
else :
  print("Fin de la tabla de multiplicar")