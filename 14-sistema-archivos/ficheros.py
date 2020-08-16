from io import open
import pathlib  

ruta = str(pathlib.Path().absolute()) + "/fichero.txt"

# Crear archivo
# archivo = open("fichero.txt","a+")

# Escribir archivo
# archivo.write("Escribiendo un archivo... \n")

# Leer archivo
archivo = open("fichero.txt","r")
# .read devuelve un string
#lectura = archivo.read()

# Recorrer cada caracter del texto
#for character in lectura:
#  print(character)

# Leer por lineas y guardarlo como list
ficheroEnLista = archivo.readlines()

for linea in ficheroEnLista:
  line = linea.split(" ")
  for word in line:
    print(word)

# Cerrar archivo
archivo.close()