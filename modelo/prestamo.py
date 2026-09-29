# logica prestamo

from datos.database import conectar
from modelo.usuario import Usuario
from modelo.libro import Libro

class Prestamos:
    def __init__(self):
        self.conexion = conectar()
        self.cursor = self.conexion.cursor()


    def prestar_libro(self, id_usuario, id_libro):
        usuario = Usuario()
        resultado = usuario.buscar_usuario_id(id_usuario)
        
        if resultado is None:
            raise ValueError('Este usuario no existe')
        
        
        ojt_libro = Libro()
        libro = ojt_libro.buscar_libro_id(id_libro)
        
        if libro is None:
            raise ValueError('El libro no existe')
        
        if not libro[1]:
            raise ValueError('El libro no esta disponible')
        
        sql_prestamo = '''
        INSERT INTO prestamos(id_usuario, id_libro, fecha_prestamo)
        
        VALUES(%s,%s,CURDATE())
        '''
        
        self.cursor.execute(sql_prestamo,(id_usuario,id_libro))
        
        sql_actualizar = '''
        UPDATE libros
        SET disponible = FALSE
        WHERE id = %s
        '''
        
        self.cursor.execute(sql_actualizar,(id_libro,))
        self.conexion.commit()
        
        return 'Prestamo realizado'
        
        
    def devolver_libro(self, id_prestamo):
        sql_prestamo = '''
        SELECT id, fecha_devolusion from prestamos WHERE id = %s
        '''
        
        self.cursor.execute(sql_prestamo,(id_prestamo,))
        prestamo = self.cursor.fetchone()
        
        if prestamo is None:
            raise ValueError('El prestamo no esta registrado')
        
        if not prestamo[1] is None:
            raise ValueError('El libro ya tiene fecha de devolusion')
        
        
        sql_devolucion = '''
        UPDATE prestamos 
        SET fecha_devolusion = CURDATE()
        WHERE id = %s
        '''
        
        self.cursor.execute(sql_devolucion,(id_prestamo,))
        
        
        sql_libro_id = '''
        SELECT id_libro from prestamos WHERE id = %s
        '''
        
        self.cursor.execute(sql_libro_id,(id_prestamo,))
        libro = self.cursor.fetchone()
        
        sql_actualizar = '''
        UPDATE libros
        SET disponible = TRUE
        WHERE id = %s
        '''
        
        self.cursor.execute(sql_actualizar,(libro[0],))
        self.conexion.commit()
        
        
    def mostrar_libros_prestados(self):
        sql_prestados = '''
        SELECT * FROM prestamos WHERE fecha_devolusion is NULL
        '''
        
        self.cursor.execute(sql_prestados)
        libros_prestados = self.cursor.fetchall()
        
        return libros_prestados
            
            
            