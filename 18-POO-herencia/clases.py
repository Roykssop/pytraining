class Persona:
  
  def getNombre(self):
    return self.nombre 

  def setNombre(self,nombre):
    self.nombre = nombre

  def getApellido(self):
    return self.nombre 

  def setApellido(self,nombre):
    self.nombre = nombre


  def getEdad(self):
    return self.nombre 

  def setEdad(self,nombre):
    self.nombre = nombre

  def caminar(self):
    return "Estoy caminando"

  def dormir(self):
    return "Estoy durmiendo"  

class Informatico(Persona):

  def __init__(self):
    self.lenguajes = ["Java","Javascript","C#"]
    self.experiencia = 5  

  def getLenguajes(self):
    return self.lenguajes

  def setLenguajes(self, lenguajes):
    self.lenguajes = lenguajes

  def getExperiencia(self):
    return self.experiencia

  def setExperiencia(self,experiencia):
    self.experiencia = experiencia

  def programar(self):
    return "Estoy programando"

class Devops(Informatico):

  def __init__(self):
    super().__init__()
    self.numeroDeploys = 50

  def deployar(self):
    return "Estoy deployando un proyecto"