import os
from Dominio.Pelicula import Pelicula
class CatalogoPeliculas(Pelicula):
    
    ruta_archivo = 'películas.txt'

    @classmethod
    def Agregar_Pelicula(cls,pelicula):
        with open(cls.ruta_archivo,'a',encoding='utf8') as archivo:
            archivo.write(f'{pelicula.nombre}\n')
    
    @classmethod
    def listar_pelicula(cls):
        with open(cls.ruta_archivo,'r',encoding='utf8') as archivo:
            print('Lista de Pelicula'.center(50,'-'))
            print(archivo.read())
    
    @classmethod
    def Eliminar(cls):
        os.remove(cls.ruta_archivo)
        print(f'Archivo Eliminado:{cls.ruta_archivo}')
        
            
