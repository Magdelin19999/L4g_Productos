# lbrerias
# lib o archivos pribados
from config import configuracionDB

DB = configuracionDB.DB

def obtenerTodosDB():
    dataProducts = []
    cursor= DB.cursor(dictionary=True)
    cursor.execute('''
        SELECT * FROM productos;''')
    dataProducts = cursor.fetchall()
    DB.commit()
    cursor.close()
    return dataProducts

def insertarNuevoDB(nombre, price):
    print('insertando a DB')
    cursor = DB.cursor()
    cursor.execute(f"insert into productos(nombre, price) values('{nombre}', {price})")
    cursor.close()
#pai
def obtenerPorIDDB(id):
    print('bsucandoo...')
    dataProducts = []
    cursor= DB.cursor(dictionary=True)
    cursor.execute(f'''
        SELECT * FROM productos WHERE id={id};''')
    dataProducts = cursor.fetchall()
    DB.commit()
    cursor.close()
    return dataProducts

def actualizarProductoDB(id,nombre, price):
    print('actualizando datoss')
    cursor = DB.cursor()
    cursor.execute(f"UPDATE productos SET nombre = '{nombre}', price = {price} WHERE id = {id}")
    cursor.close()

def eliminarIDDB(id):
    cursor = DB.cursor()
    cursor.execute(f"Delete FROM productos where id={id}")
    cursor.close()
