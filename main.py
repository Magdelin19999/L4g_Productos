from flask import *

from controllers import manipulacionDB

app = Flask(__name__)

@app.get('/')
def home():
    return render_template('productos/index.html', productos = manipulacionDB.obtenerTodos())

# redireccionamiento del html
@app.get('/registro-productos')
def regitroProducto():
    return render_template('productos/registraProducto.html')

# metodo que se llama al dar guardar del formulario
@app.post('/registro-productos')
def crearProducto():
    print('registro producro')
    nombre = request.form.get('inputNombre')
    price = request.form.get('inputPrice')
    print(nombre,price)
    manipulacionDB.insertarNuevo(nombre, price)
    return redirect(url_for('home'))
 

@app.get('/editar-producto/<int:id>')
def editarProducto(id):
    producto = manipulacionDB.obtenerPorID(id)
    return render_template('productos/editarProducto.html',producto = producto[0])

@app.post('/editar-producto')
def editarProductoForm():
    print('registro producro')
    id = request.form.get('inputID')
    nombre = request.form.get('inputNombre')
    price = request.form.get('inputPrice')
    print(nombre,price)
    manipulacionDB.actualizarProducto(id, nombre, price)
    return redirect(url_for('home'))
 
@app.get('/eliminar-producto/<int:id>')
def eliminarProducto(id):
    manipulacionDB.eliminarID(id)
    return redirect(url_for('home'))
 
    
app.run(
        debug=True,
        host='localhost',
        port=4500
        )