"""con from llamamos la libreria de flask
con el import se llama al elemento de la biblioteca
render_template este elemento permite agregar rutas html al proyecto"""
from flask import Flask, render_template

"""inicializar flask
se guarda lo que devuelve el flask en un objeto"""
app = Flask(__name__)

"""crear rutas del servidor
la pagina principal la definimos con el /"""
@app.route('/')
#funcion que devuelve la vista del usuario
def home():
    return render_template('home.html')

#crear nueva ruta
@app.route('/institucional')
def institucional():
    return render_template('institucional.html')

@app.route('/inventario')
def inventario():
    return render_template('inventario.html')

@app.route('/productos')
def productos():
    return render_template('productos.html')

#dejar la pagina escuchando, lista para peticiones
if __name__ == '__main__':
    #este medoto permite iniciar la aplicacion
    app.run(debug=True)