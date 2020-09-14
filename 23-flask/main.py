from flask import Flask 

app = Flask(__name__)

# Definimos la ruta base
@app.route('/')
# Asociamos el route con la función inmediatamente definida
def index():
  return "Aprendiendo Flask" 

@app.route('/contacto')
# Es válido retornar html
def contacto():
  return "<h1> Página de contacto</h1>"  

@app.route('/informacion/')
@app.route('/informacion/<string:nombre>')
@app.route('/informacion/<string:nombre>/<int:dato>')
def informacion(nombre = None,dato = None):
  ret = ""

  if(nombre != None and dato != None):
    ret = f"Parámetros: El nombre es {nombre}, y el dato requerido: {dato}"

  return ret

@app.route('/lenguajes-de-programacion')
# Es válido retornar html
def lenguajes():
  return "<h1> Página de lenguajes</h1>"  


# Corremos la app en debug true
if __name__ == '__main__':
  app.run(debug=True)