
from Computadora import Computadora
class Orden(Computadora):
    
    id_orden = 0
    @classmethod
    def Contador_Ordenes(cls):
        cls.id_orden+=1
        return cls.id_orden
    
    def __init__(self, computadora) -> None:
        self.id_computadora = Orden.Contador_Ordenes()
        self._computadora = computadora
    
    def Agregar_Computadora(self,agregando):
        self._computadora.append(agregando)
    
    def __str__(self) -> str:
        lista_computadora = ''
        for computador in self._computadora:
            lista_computadora+=computador.__str__()
        return f'''
            Orden:[{self.id_computadora}]
            COMPUTADORA:{lista_computadora}
        '''

