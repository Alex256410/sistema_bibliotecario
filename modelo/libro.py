# logica de libro.py


class Libro:
    def __init__(self, conexion):
        self.conexion = conexion
        self.cursor = conexion.cursor()
        
    def ingresar_libro(self, titulo, autor):
        scrip_usuario = '''
        INSERT INTO libros(titulo, autor) VALUES(%s,%s)
        '''
        
        self.cursor.execute(scrip_usuario,(titulo, autor))
        self.conexion.commit()
    
    def buscar_libro_id(self, id_libro):   
        sql_libro = '''
        SELECT id, disponible
        FROM libros
        WHERE id = %s
        '''

        self.cursor.execute(sql_libro, (id_libro,))

        libro = self.cursor.fetchone()
        
        return libro
    
    def mostrar_libros(self):
        sql_libros = '''
        SELECT * FROM libros WHERE disponible = TRUE
        '''
        
        self.cursor.execute(sql_libros)
        libro = self.cursor.fetchall()
        
        return libro        