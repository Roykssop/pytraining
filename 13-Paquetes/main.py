"""
  Un paquete me permite englobar una serie de módulos,
  lo cual me ayuda a poder hacer todo este grupo de módulos reusable y
  mantener el código mas ordenado
  Se crea una carpeta con el nombre del paquete
  y adentro un archivo __init__.py y los demás módulos.
"""

from paquete import buenosdias, tunombre

buenosdias.darBuenosDias("Hernan")
tunombre.darNombreCompleto("Jacky","Sieras")