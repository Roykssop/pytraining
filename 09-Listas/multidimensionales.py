# Lista multidimensional

listaFruteria = [
  ["Naranja", "Anaranjado"],
  ["Manzana", "Roja"],
  ["Zandía", "Verde"]
]

# Accediendo a los colores de las frutas
print(listaFruteria[0][1])
print(listaFruteria[1][1])
print(listaFruteria[2][1])

# Iterando Lista multidimensional

for frutas in listaFruteria:
  for fruta in frutas:
    if frutas.index(fruta) == 0:
      print(f"{frutas.index(fruta)}. Nombre de fruta: {fruta}")
    else:
      print(f"{frutas.index(fruta)}. Color de fruta: {fruta}") 
  print("\n")     