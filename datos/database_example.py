import mariadb

def conectar():
    return mariadb.connect(
        host='localhost',
        user='TU_USUARIO',
        password='TU_PASSWORD',
        database='biblioteca'
    )