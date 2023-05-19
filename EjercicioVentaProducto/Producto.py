class Producto:

    contador_producto = 0
    @classmethod
    def Generar_Contador(cls):
        cls.contador_producto +=1
        return cls.contador_producto
    
    def __init__(self, nombre, precio) -> None:
        self.id_producto = Producto.Generar_Contador()
        self.nombre = nombre
        self._precio = precio
    
    @property
    def precio(self):
        return self._precio

    def __str__(self) -> str:
        return f'''
                id_Producto[{self.id_producto}]
                Nombre: {self.nombre}
                Precio:{float(self._precio)}
        
        '''
    
if __name__=='__main__':
    producto1 = Producto('Short',3.50)
    print(producto1)

    print (f'SEPARADOR'.center(50,'-'))
    producto2 = Producto('Camisa',8.50)
    print(producto2)

    print(f'Genera_Contador_Venta[{Producto.contador_producto}]')
