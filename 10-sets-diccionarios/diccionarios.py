"""
  Este tipo de dato almacena el conjunto de datos clave/valor,
  simil a array asociativo.
"""
# Definicion diccionario
usuario = {
  "nombre": "Hernan",
  "nacionalidad": "Argentino"
}

# imprime class <class 'dict'>
print(type(usuario))


# Imprimir determinada clave
print(usuario["nacionalidad"])

# Juntando listas con diccionarios

contactos = [
  {
    "nombre": "Hernan",
    "nacionalidad": "Argentino"    
  },
  {
    "nombre": "Diogo",
    "nacionalidad": "Brasileño"
  },
  {
    "nombre": "Jaime",
    "nacionalidad": "Mexicano"
  }
]

# Cambio valor de lista/diccionario
contactos[1]["nombre"] = "Joao"

# Imprimo un valor de la lista/diccionario
print(contactos[1]["nombre"])

# Recorro lista/diccionario
print("Lista de contactos")
print("=====================================")
for contacto in contactos:
  print(f"Nombre: {contacto['nombre']}")
  print(f"Nombre: {contacto['nacionalidad']}")
  print("=====================================")



