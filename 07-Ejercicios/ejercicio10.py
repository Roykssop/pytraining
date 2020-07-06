"""
  Tomar la nota de 15 alumnos, y decir cuantos han aprobados
"""

notaApta = int(input("Ingrese a partir de que nota se considera aprobado: "))
contador = 1
aprobados = 0
suspendidos = 0

print("Ingresará la nota de los 15 alumnos del curso")

while contador <= 15:
  nota = int(input(f"Ingrese la nota del alumno {contador}: "))
  if nota >= notaApta:
    aprobados += 1
  else:
    suspendidos += 1

  contador += 1
else:
  print(f"Los aprobados fueron {aprobados}")
  print(f"Los suspendidos fueron {suspendidos}")