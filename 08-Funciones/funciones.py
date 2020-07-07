"""
  Funciones
"""

# Función sin parámetros
def helloWorld():
  print("Hello World")

# Función muestra nombre
def muestraNombre(nombre):
  print(f"Su nombre es: {nombre} ")

# Muestra tabla de multiplicar
def muestraTabla(num = 1):
  print(f"######## Tabla de multiplicar del {num} #################")
  for contador in range(11):
    print(f"El resultado de {num} x {contador} es : {num * contador} ")

# Llamada primer función
helloWorld()

# Llamada funcion muestraNombre
muestraNombre("Hernan")

# Llamada función muestraTabla
muestraTabla(10)
muestraTabla()


