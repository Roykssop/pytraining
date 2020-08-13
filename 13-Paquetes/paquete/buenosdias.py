import datetime

def darBuenosDias(nombre):
  diaCompleto = datetime.datetime.now() 
  diaFormateado = diaCompleto.strftime("%d/%m/%Y") 
  print(f"Muy buenos días {nombre} !! hoy es { diaFormateado }")