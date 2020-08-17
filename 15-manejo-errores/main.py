"""
  Capturar excepciones y manejar erroresen código
  susceptible a fallos/errores
"""

try:
  numero = input("Ingrese un número: ")
  numero2 = input("Ingrese otro número: ")
  suma = numero * numero2 

  print(f"La multiplicación final es: {suma} ")
except:
  print(f"Error en la ejecución del programa")
finally:
  print(f"Finalizó el programa")