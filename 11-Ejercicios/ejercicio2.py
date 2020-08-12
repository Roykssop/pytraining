"""
  Escribir un programa que añada valores a una lista mientras que su longitud
  sea menor a 120 , while && for
"""

longitud = 120
lista = []
count = 0
array = [] 

while len(lista) < 120:
  lista.append(count);
  count+= 1

for counter in range(120):
  array.append(counter)

print(array)
