"""
  Son funcionalidades ya hechas para reutilizar.

  Por defecto ya vienen muchos modulos con el core de python.
  https://docs.python.org/3/py-modindex.html
"""
# Importo el módulo
import mimodulo

# Importo una función sola de mi modulo
# from mimodulo import holaModulo

# Importo todas las funciones
# from mimodulo import *

print(mimodulo.holaModulo("mimodulo"))


# ====== Modulo fechas ========
import datetime

# Fecha
print(datetime.date.today())

# Fecha completa
fechacompleta = datetime.datetime.now()
print(fechacompleta)

# Año
print(fechacompleta.year)

# Mes
print(fechacompleta.month)

# Día
print(fechacompleta.day)

# Día formateado
print(fechacompleta.strftime("%d/%m/%Y"))

# ====== Modulo Math ========
import math

# Raíz cuadrada de un número
print("Raiz cuadrada de 16", math.sqrt(16))

# Número π
print("Valor de π", math.pi)

# Redondear a la baja un número
print("Redondeo a la baja- de 15.9", math.floor(15.9))

# Redondear al alza un número
print("Redondeo a la baja- de 15.9", math.ceil(15.9))

# ====== Modulo Random ========
import random

# Número random entre 2 extremos
print("El número entre 30 y 80 es:", random.randint(30,80))
