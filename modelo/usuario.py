# logica de usuario.py


from datos.database import conectar

class Usuario:
    def __init__(self):
        self.conexion = conectar()
        self.cursor = self.conexion.cursor()
    
    def ingresar_usuario(self, nombre, email):
        sql_usuario = '''
        INSERT INTO usuario(nombre, email) VALUES(%s,%s)
        '''
        
        self.cursor.execute(sql_usuario,(nombre, email))
        self.conexion.commit()
     
    def buscar_usuario_id(self, id_usuario):   
        sql_usuario = '''
        SELECT id
        FROM usuario
        WHERE id = %s
        '''

        self.cursor.execute(sql_usuario, (id_usuario,))
        usuario = self.cursor.fetchone()
        
        
        return usuario



        
    








