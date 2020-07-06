"""
  Ingresar numero y el porcentaje que le queremos calcular
"""

numero = int(input("Ingrese un número por favor: "))
porcentaje = int(input("Ingrese porcentaje a calcular: "))

print(f"El {porcentaje}% de {numero} es: { ( porcentaje * numero ) / 100 }")