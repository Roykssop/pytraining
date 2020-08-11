frutas=['Manzana','Naranja','Banana','Uva']
vegetales=['Rucula','Espinaca','Lechuga']

# Ordenar
print(frutas)
frutas.sort()
print(frutas)

# Agregar item
frutas.insert(1,'Pera')

# Eliminar elementos
frutas.pop(0)
vegetales.remove('Lechuga')
print(frutas)
print(vegetales)

# Contar elementos
print(len(vegetales))


# Cuantas veces aparece x elemento
print(vegetales.count('Espinaca'))

# Invertir array
frutas.reverse()
print(frutas)

# Buscar elemento dentro de una lista
print('Pera' in frutas)

# Obtener índice
print(frutas.index('Pera'))

# unir listas
frutas.extend(vegetales)
print(f'Lista unida {frutas} ')