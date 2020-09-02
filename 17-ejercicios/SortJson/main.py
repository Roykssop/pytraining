"""
 Jul 23
Listar alfabéticamente de manera ascendente por apellido los empleados que están almacenados en un archivo JSON como el que sigue, indicando los skills del empleado. 
"""
from io import open
import json

archivo = open('empleados.json',"r")
jsonFile = json.load(archivo)
dictOrdered = sorted(jsonFile, key=lambda k: k['lastname']) 

print("Lista de empleados:")
print("===================")
for employee in dictOrdered:
  print(f"Empleado:{employee['name']} {employee['lastname']}, Skills: {employee['skills']}")

