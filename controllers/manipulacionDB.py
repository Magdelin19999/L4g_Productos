import imp
from models import senteciasSQL

def obtenerTodos():
    return senteciasSQL.obtenerTodosDB()

def insertarNuevo(nombre, price):
    print('envido a modelos')
    senteciasSQL.insertarNuevoDB(nombre, price)

    #seleini
def obtenerPorID(id):
    print('buscando...')
    return senteciasSQL.obtenerPorIDDB(id)

def actualizarProducto(id,nombre, price):
    print('enviando datoss')
    senteciasSQL.actualizarProductoDB(id,nombre,price)
    
def eliminarID (id):
    senteciasSQL.eliminarIDDB(id)
     