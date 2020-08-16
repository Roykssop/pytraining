from io import open
import pathlib  

ruta = str(pathlib.Path().absolute()) + "/fichero.txt"
archivo = open("fichero.txt","a+")

archivo.write("Escribiendo un archivo... \n")
