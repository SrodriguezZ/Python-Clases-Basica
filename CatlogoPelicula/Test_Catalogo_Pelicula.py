from Dominio.Pelicula import Pelicula
from Servicio.CatalogoPeliculas import CatalogoPeliculas as cp

opcion = None
while opcion !=4:
    try:
        print('Opciones: ')
        print('''
        1.Agregar Pelicula
        2.Listar Peliculas
        3.Eliminar Catalogo Pelicula
        4.Salir
        ''')
        opcion = int(input('Ingrese la opcion(1-4): '))
        if opcion == 1:
            nombre_pelicula = input('Proporcione el nombre de la pelicula: ')
            pelicula = Pelicula(nombre_pelicula)
            cp.Agregar_Pelicula(pelicula)
        elif opcion ==2:
            cp.listar_pelicula()
        elif opcion ==3:
            cp.Eliminar()
        else:
            opcion = 4
            print('Salimos del ciclo')
        
                        
    except Exception as e:
        print('Ocurrió un error:{e}')
else:
    print('Salimos del Programa')