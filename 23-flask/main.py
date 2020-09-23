from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

# Definimos la ruta base
@app.route('/')
# Asociamos el route con la función inmediatamente definida
def index():
  return render_template('index.html')

@app.route('/informacion/')
@app.route('/informacion/<string:nombre>')
@app.route('/informacion/<string:nombre>/<int:dato>')
def informacion(nombre = None,dato = None):
  ret = ""

  if(nombre != None and dato != None):
    ret = f"Parámetros: El nombre es {nombre}, y el dato requerido: {dato}"

  return render_template('informacion.html', texto=ret)

@app.route('/lenguajes-de-programacion')
# Es válido retornar html
def lenguajes():
  return render_template('lenguajes.html')

@app.route('/contacto')
@app.route('/contacto/<redireccion>')
# Hacemos una redireccion
def contacto(redireccion=None):
  if redireccion is not None:
    return redirect(url_for('lenguajes'))

  return render_template('contacto.html')  


# Corremos la app en debug true
if __name__ == '__main__':
  app.run(debug=True)