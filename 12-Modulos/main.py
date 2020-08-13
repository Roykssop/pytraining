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


# Modulo fechas
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