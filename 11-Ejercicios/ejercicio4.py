"""
  Crear un script que tenga 4 variables,de tipo lista, string, entero y booleano
  imprimir un mensaje segun el tipo de cada variable. Usar funciones
"""

def devuelveTipo( var ):
  mensaje = "La variable no es de ninguno de los tipos del ejercicio"

  tipos = [
    {
      "tipo": bool,
      "mensaje": "La variable es booleana"
    },
    {  
      "tipo": list,
      "mensaje": "La variable es una lista"
    },
    {
      "tipo": str,
      "mensaje": "La variable es un string"
    },
    {
      "tipo": int,
      "mensaje": "La variable es un entero"
    }            
  ]

  for tipo in tipos: 
    if isinstance(var, tipo["tipo"]):
      mensaje = tipo["mensaje"]
      break

  return mensaje


lista = []
texto = "Hello world"
numero = 1020
booleno = False 

print(devuelveTipo(lista))
print(devuelveTipo(texto))
print(devuelveTipo(numero))
print(devuelveTipo(booleno))