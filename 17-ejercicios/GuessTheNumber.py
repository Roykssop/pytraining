import random

class GuessTheNumber:

  __i = 0
  __resultado = "Has perdido el juego"

  def __init__(self,attempts,topNumber):
    self.__attempts = attempts
    self.__topNumber = topNumber
    self.__numberToGuess = random.randint(1,topNumber)

  def isWinner(self,num):
    return num == self.__numberToGuess

  def getLeftAttempts(self,currentAttempt):
    return self.__attempts - currentAttempt

  def startGame(self):
    for i in range(self.__attempts):
      while True:
        try:  
          numero=int(input(f"Adivine el número de 1 a { self.__topNumber }, tiene { self.getLeftAttempts(i) } intentos: "))
          if(numero < 1 or numero > self.__topNumber):
            raise ValueError("Ingrese un numero dentro del rango de 1 a 20 por favor")   
          break
        except ValueError:
          print("Ingresa un número correcto")

      if(self.isWinner(numero)):
        self.__resultado = "Adivinaste el número!"
        break

    print(self.__resultado)