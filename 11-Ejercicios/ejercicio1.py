# Fn recorre lista
def recorreListaSimple( nombre, lista ):
  print(f"============= {nombre} ===========")
  for item in lista:
    print(item)
  print("===============================\n")

def devuelveElemento( indice, lista ):
  if( indice < len(lista) ):
    print(lista.index(indice))
  else:
    print("No existe el elemento")

# Crear lista con 8 números
numlist = list(range(8,0,-1)) 

# Recorrerla y mostrarla
recorreListaSimple("Lista desordenada",numlist)

# Ordenarla y mostrarla
numlist.sort()
recorreListaSimple("Lista ordenada",numlist)

# Mostrar su longitud
print(f"Longitud de la lista {len(numlist)}")

# Buscar un elemento en base a lo que nos pida el usuario por teclado
try:
  value = int(input("Ingrese el indice de la lista que quiere ver... :"))  
  devuelveElemento(value, numlist)
except:
  print("Error")