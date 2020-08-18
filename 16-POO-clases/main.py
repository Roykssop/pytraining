class Coche:
  marca="Ford"
  modelo="Focus"
  year=2010
  color="Verde"
  puertas=4
  velocidad=300

  def getMarca(self):
    return self.marca

  def setMarca(self,marca):
    self.marca = marca

  def getModelo(self):
    return self.modelo

  def setModelo(self,modelo):
    self.modelo = modelo

  def getYear(self):
    return self.year

  def setYear(self,year):
    self.year = year

  def getColor(self):
    return self.color

  def setColor(self, color):
    self.color = color
  
  def getPuertas(self):
    return self.puertas

  def setPuertas(self, puertas):
    self.puertas = puertas

  def getVelocidad(self):
    return self.velocidad

  def setVelocidad(self,velocidad):
    self.velocidad = velocidad

  def acelerar(self):
    self.velocidad += 1

  def frenar(self):
    self.velocidad -= 1


# Fin class Coche

#
#   Definicion coche 1
#
coche1 = Coche()

# Imprimir props básicas
coche1.setMarca("Lamborghini")
coche1.setModelo("Diablo")
coche1.setPuertas(2)
coche1.acelerar()
coche1.acelerar()
coche1.frenar()
print("Coche 1",coche1.getMarca(), coche1.getModelo(), coche1.getYear(), coche1.getVelocidad())

# Definicion coche 2
coche2 = Coche()
coche2.setMarca("Ford")
coche2.setModelo("Fiesta")
coche2.setPuertas(4)
coche2.setYear(2017)
coche1.acelerar()
coche1.acelerar()
coche1.acelerar()
coche1.frenar()
print("Coche 2",coche2.getMarca(), coche2.getModelo(), coche2.getYear(), coche2.getVelocidad())
