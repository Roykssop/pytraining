"""
  Generar un numero aleatorio entre 1 y 20, pedirle al user que lo adivine en no mas de 6 intentos
"""

from GuessTheNumber import GuessTheNumber

juego = GuessTheNumber(6,20)
juego.startGame()