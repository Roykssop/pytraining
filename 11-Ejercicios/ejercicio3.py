"""
  Comprobar si una variable esta vacia, si es así rellenarla con texto en minúscula
  y mostrarlo en mayúscula
"""
frase = "    "

if (len(frase.strip()) == 0): 
  print("Variable vacia")
  frase = "Para que nada nos separe que nada nos una."
  frase.upper()
  print(f"Frase: {frase}")
else:
  print("Variable con contenido")