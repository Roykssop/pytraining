"""
  Capturar excepciones y manejar erroresen código
  susceptible a fallos/errores
"""

"""
#  Manejo básico de excepciones

try:
  numero = input("Ingrese un número: ")
  numero2 = input("Ingrese otro número: ")
  suma = numero * numero2 

  print(f"La multiplicación final es: {suma} ")
except:
  print(f"Error en la ejecución del programa")
finally:
  print(f"Finalizó el programa")
"""

"""
  Manejo de múltiples errores


# Imprimo nombre del tipo
print(type(9).__name__)

try:
  numero = int(input("Ingrese un número para elevarlo al cuadrado: "))
  print(f"La multiplicación final es:"+str(numero*numero) )
except TypeError:
  print("Debes convertir tus cadenas a enteros en el código")
except ValueError:
  print("Introduce un número correcto!")
except Exception as e:
  print("Ha ocurrido unn error", type(e).__name__)

"""

"""
  Lanzando excpeciones personalizadas
"""
try:
  if edad < 5 or edad > 110:
    raise ValueError("La edad introducida no es real")
  elif len(nombre) <= 1:
    raise ValueError("El nombre no es correcto")
except:
  print("Ingrese los datos correctamente")