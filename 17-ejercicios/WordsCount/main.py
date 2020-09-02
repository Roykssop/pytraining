"""
Contar las ocurrencias de cada palabra en una frase dada, y listar los resultados como:
<palabra>: <ocurrencias>;   donde <palabra> es cada palabra distinta que compone la frase, y
                            <ocurrencias> es la cantidad de veces que tal palabra aparece.

Consideraciones para el parsing:
- case insensitive (a los efectos de contar "Python", "PYTHON" y "python", se consideran la misma palabra).
- los signos de puntuación se ignoran.
- las palabras pueden estar separadas por cualquier tipo y cantidad de blancos (" ", "   ", "\t", "\n", ...).
"""

import re
from collections import Counter

phrase = "Al final todo va a salir Bien. Si no ha salido bien, es que todavía no es el final"
words = re.split(r"[,.;:\s]+",phrase.upper())
c = Counter(words) 

print("Listado de palabras y sus ocurrencias")
print("=====================================")
for word in c:
  print(f" {word}: {c[word]} ")