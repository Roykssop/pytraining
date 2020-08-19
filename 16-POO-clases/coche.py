class Coche:
  marca="Ford"
  modelo="Focus"
  year=2010
  color="Verde"
  puertas=4
  velocidad=300

  def __init__(self,marca,modelo,year,color,puertas,velocidad):
    self.marca = marca
    self.modelo = modelo 
    self.year = year
    self.color = color 
    self.puertas = puertas 
    self.velocidad = velocidad

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

  def getInfo(self):
    info = "Información del Coche: \n"
    info += "======================"
    for key,val in self.__dict__.items():
      info += f"\n{key} : {val} "
    
    return info