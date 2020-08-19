from coche import Coche


# Fin class Coche

#
#   Definicion coche 1
#
coche1 = Coche("Ferrari","Testarrosa","2012","rojo",2,400)

# Imprimir props básicas
print(coche1.getInfo())


# Definicion coche 2
coche2 = Coche("Ford","Fiesta","2017","blanco",4,250)
coche2.setMarca("Ford")
coche2.setModelo("Fiesta")
coche2.setPuertas(4)
coche2.setYear(2017)
coche1.acelerar()
coche1.acelerar()
coche1.acelerar()
coche1.frenar()
print(coche2.getInfo())