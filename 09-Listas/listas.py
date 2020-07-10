"""
  Podemos crear listas, que pueden contener
  distintos tipos de datos.
"""
listaNumeros = [1,2,3,4,5]
listaFrutas = list(('Manzana','Banana','Pera','Naranja'))
listaMixed = list((1,10.5,[1,2,3],'Texto',True))
listaRango =list(range(2000,2020))


# Imprimiendo listas
# print(listaNumeros)
# print(listaFrutas)
# print(listaMixed)
# print(listaRango)

# Imprimiendo subsets de las listas 
print(listaRango[:3]) # Imprime los valores desde el inicio al indice 3
print(listaRango[5:]) # Imprime los valores desde el indice 5
print(listaRango[-5:]) # Imprime los valores últimos 5 índices
print(listaRango[1:3]) # Imprime los valores de los índices 1 y 2
print(listaRango[1]) # Imprime valor de índice 1

# Recorriendo Los valores de la lista
# Sumamos 1 a cada valor
for contador in range(len(listaRango)):
  listaRango[contador] = listaRango[contador] + 1

# Recorriendo los valores de otra forma
for fruta in listaFrutas:
  print(fruta)

# Agregamos un item a la lista
listaRango.append(2021)

print(listaRango)

