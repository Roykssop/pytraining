"""
 Scope de variables,
"""

varGlobal = "Esto es una variable global"

def usoVariableGlobal():
  print(varGlobal)
  varLocal = "Esta variable solo existe dentro de la func"
  print(varLocal) 
  global varConvertidaAGlobal
  varConvertidaAGlobal = "Esta variable fue convertida a global"

usoVariableGlobal()
print(varConvertidaAGlobal)

