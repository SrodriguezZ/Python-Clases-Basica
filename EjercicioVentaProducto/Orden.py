from Producto import Producto
class Orden(Producto):

    Contador_Ordenes = 0
    @classmethod
    def Generador_Contador(cls):
        cls.Contador_Ordenes+=1
        return cls.Contador_Ordenes
    
    def __init__(self, productos) -> None:
        self._id_ordenes = Orden.Generador_Contador()
        self._productos = list(productos)

    def Agregar_Producto(self, producto):
        self._productos.append(producto)

    def Calcular(self):
        total = 0
        for producto in self._productos:
            total += producto._precio
        return total
    
    def __str__(self) -> str:
        productos_str = ''
        for producto in self._productos:
            productos_str+=producto.__str__() + '♦'
        
        return f'Orden: {self._id_ordenes}, \nProductos {productos_str}'
    
if __name__=='__main__':
    producto1 = Producto('Blusa',3.50)
    producto2 = Producto('Short',8.50)
    Productos1=[producto1,producto2]
    orden1 = Orden(Productos1)
    print(orden1)
    producto3=Producto('Zapatos',75)
    producto4 = Producto('Cinturón',1.50)
    Productos2=[producto3,producto4]
    orden2 =Orden(Productos2)
    print(orden2)