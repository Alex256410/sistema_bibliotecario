from datos.database import conectar
from modelo.libro import Libro
from modelo.usuario import Usuario
from modelo.prestamo import Prestamos
import textwrap # evita identacion innecesaria en el print
conexion = None

try:
    conexion = conectar()
    usuario = Usuario(conexion)
    libro = Libro(conexion)
    prestamo = Prestamos(conexion,usuario,libro)


    print('=' * 22)
    print('Sistema Bibliotecario')
    print('=' * 22 + '\n')

    while True:
        print('Opciones')
        print('=' * 50 + '\n')
        print('1. Registar usuario')
        print('2. Registar libro')
        print('3. Mostrar libros disponibles')
        print('4. Mostar libros prestados y devueltos')
        print('5. Prestamos y devolusion de libros')
        print('6. Salir')
        print('=' * 50 + '\n')
        
        opcion = input('Elige una opcion: ').strip()
        
        if opcion == '1':
            print('\nRegistre su usuario\n')
            
            nombre = input('Ingrese su nombre: ').strip().capitalize()
            email = input('Ingrese su email: ').strip()
            
            usuario.ingresar_usuario(nombre, email)
            print('\nRegistro realizado con exito\n')
            
        elif opcion == '2':
            print('\nRegistro de libro\n')
            
            titulo = input('Titulo del libro: ').strip().capitalize()
            autor = input('Nombre del autor del libro: ').strip().capitalize()

            libro.ingresar_libro(titulo, autor)
            print('\nLibro ingresado con exito\n')
            
        elif opcion == '3':
            libros = libro.mostrar_libros()
            
            if libros is None:
                print('\nNo hay libros disponibles\n')
                
            else:
                print('\nLibros disponibles:\n')
                for libro in libros:
                    texto = f'''
                    ID: {libro[0]}
                    Titulo: {libro[1]}
                    Autor: {libro[2]}
                    Disponible: {libro[3]}
                    '''
                    print(textwrap.dedent(texto))
    

            
        elif opcion == '4':
            while True:
                print('\n1. Libros prestados')
                print('2. Libros devueltos')
                print('3. Volver al menu principal\n')
                
                opcion = input('\nElige una opcion: ')
                
                if opcion == '1':
                    try:
                        libros_prestados = prestamo.mostrar_libros_prestados()
                        
                        if not libros_prestados:
                            print('No hay libros prestados')
                        else:
                            for prestado in libros_prestados:
                                texto = f'''
                                    ID: {prestado[0]}
                                    Usuario: {prestado[1]}
                                    Libro: {prestado[2]}
                                    Fecha de prestamo: {prestado[3]}
                                    '''
                                print(textwrap.dedent(texto))
                    except ValueError as e:
                        print(e)
                
                elif opcion == '2':
                    try:
                        libros_devueltos = prestamo.mostrar_libros_devueltos()
                        
                        if not libros_devueltos:
                            print('No hay libros devueltos')
                        else:
                            for devuelve in libros_devueltos:
                                texto = f'''
                                    ID: {devuelve[0]}
                                    Usuario: {devuelve[1]}
                                    Libro: {devuelve[2]}
                                    Fecha de prestamo: {devuelve[3]}
                                    Fecha de devolucion: {devuelve[4]}
                                    '''
                                print(textwrap.dedent(texto))
                    except ValueError as e:
                        print(e)
                        
                elif opcion == '3':
                    break
                
                else:
                    print('\nAsegurese de elegir 1 de las 3 opciones\n')
                    
                
                        
        elif opcion == '5':
            while True:
                print('\n1. Prestar libro')
                print('2. Devolver libro')
                print('3. Volver al menu principal')
                
                opcion = input('\nElige una de las 3 opciones: ').strip()
                
                if opcion == '1':
                    try:
                        print('\nAparte su libro aqui')
                        id_usuario = input('Ingrese su ID de usuario: ').strip()
                        id_libro = input('Ingrese id del libro para apartar: ').strip()
                        prestamo.prestar_libro(id_usuario, id_libro)
                        print('\nLibro apartado con exito\n')
                    except ValueError as e:
                        print(f'ERROR!: {e}')
                    
                elif opcion == '2':
                    id_prestamo = input('\nIngrese el ID del prestamo: ').strip()
                    prestamo.devolver_libro(id_prestamo)
                    print('\nLibro devuelto con exito\n')
                    
                elif opcion == '3':
                    break
                
                else:
                    print('\nPor favor eliga una de las 3 opciones')
            
        elif opcion == '6':
            print('Saliendo del programa...')
            print('Fin.')
            break

except ValueError as e:
    print(e)

finally:
    if conexion is not None:
        conexion.close()
