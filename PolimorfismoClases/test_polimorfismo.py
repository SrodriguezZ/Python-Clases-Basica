from Empleado import Empleado
from Gerente import Gerente
def imprimir_detalles(objeto):
    #print(objeto)
    print(type(objeto))
    if isinstance(objeto, Gerente):
        print(objeto.sueldo)


gerente = Gerente('Steeven',800,'Programación')
imprimir_detalles(gerente)