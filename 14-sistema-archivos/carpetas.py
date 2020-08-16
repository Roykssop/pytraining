import os
import shutil

# Crear carpeta
# os.mkdir(os.path.abspath("./") + "/carpetica")

# Evaluar si existe
if not os.path.isdir("./carpetica"):
  os.mkdir(os.path.abspath("./") + "/carpetica")
else:
  print("Ya existe el directorio")
  
# Copiar
ruta_original = "./carpetica"
ruta_nueva = "./carpetica2"

#shutil.copytree(ruta_original,ruta_nueva)

# Eliminar
# os.rmdir(ruta_nueva)

# Lista contenido de directorio
contenido = os.listdir("./carpetica")

for arch in contenido:
  print(arch)