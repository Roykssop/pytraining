"""
  Funciones
"""

# Función sin parámetros
def helloWorld():
  print("Hello World")

# Función con parámetro
def muestraNombre(nombre):
  print(f"Su nombre es: {nombre} ")

# Función parametro por defecto
def muestraTabla(num = 1):
  print(f"######## Tabla de multiplicar del {num} #################")
  for contador in range(11):
    print(f"El resultado de {num} x {contador} es : {num * contador} ")

# Funcion lambda ( Función anónima ), realizan operaciones simples
suma1 = lambda numero: numero+1




# Llamada primer función
helloWorld()

# Llamada funcion muestraNombre
muestraNombre("Hernan")

# Llamada función muestraTabla
muestraTabla(10)
muestraTabla()

# Llamado a funcion lamda
print(suma1(10))
