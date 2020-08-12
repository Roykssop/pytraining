"""
  SET es un tipo de dato, para tener una coleccion de valores,
  pero no tiene ni índice ni orden
"""

frutas = {
  "Ananá",
  "Mango",
  "Cereza"
}

frutas.add("Caqui")
frutas.remove("Mango")

# Los imprime sin un orden fijo
print(frutas)
