from Producto import Producto
from Orden import Orden

producto1 = Producto('Blusa',3.50)
producto2 = Producto('Short',8.50)
producto3=Producto('Zapatos',75)
producto4 = Producto('Cinturón',1.50)
Productos1=[producto1,producto2]
orden1 = Orden(Productos1)
orden1.Agregar_Producto(producto3)
orden1.Agregar_Producto(producto4)
print(orden1)
print(f'Valor a Pagar:[{orden1.Calcular()}]')
Productos2=[producto3,producto4]
orden2 =Orden(Productos2)
print(orden2)
print(f'Valor a Pagar:[{orden2.Calcular()}]')