from flask import Flask, redirect, url_for 

app = Flask(__name__)

# Definimos la ruta base
@app.route('/')
# Asociamos el route con la función inmediatamente definida
def index():
  return "Aprendiendo Flask" 

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

@app.route('/contacto')
@app.route('/contacto/<redireccion>')
# Hacemos una redireccion
def contacto(redireccion):
  if redireccion is not None:
    return redirect(url_for('lenguajes'))

  return "<h1> Página de contacto</h1>"  


# Corremos la app en debug true
if __name__ == '__main__':
  app.run(debug=True)