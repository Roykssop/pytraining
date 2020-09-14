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

@app.route('/lenguajes-de-programacion')
# Es válido retornar html
def lenguajes():
  return "<h1> Página de lenguajes</h1>"  


# Corremos la app en debug true
if __name__ == '__main__':
  app.run(debug=True)