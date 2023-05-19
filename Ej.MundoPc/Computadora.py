from Monitor import Monitor
from  Teclado import Teclado
from Ratón import Ratón

class Computadora(Monitor, Teclado, Ratón):
    contador_computador = 0
    @classmethod
    def Contador_Computadora(cls):
        cls.contador_computador+=1
        return cls.contador_computador
    
    def __init__(self,nombre, monitor , ratón, teclado ) -> None:
        self._id_computadora = Computadora.Contador_Computadora()
        self._nombre= nombre 
        self._monitor = monitor
        self._ratón = ratón
        self._teclado = teclado
    
    def __str__(self) -> str:
        return f'''
        ID_COMPUTADORA:[{self._id_computadora}]COMPUTADORA:[{self._nombre}]
        {self._monitor}
        {self._ratón}
        {self._teclado}
        '''

if __name__=='__main__':
    monitor1 = Monitor('LG','900')
    ratón1 = Ratón('USB','DELL')
    teclado1 = Teclado('USB','MARCA')
    computadora1 = Computadora('RICOH',monitor1,ratón1,teclado1)
    print(computadora1)

    monitor2 = Monitor('ACER','1000')
    ratón2 = Ratón('USB','DELL')
    teclado2 = Teclado('INALÁMBRICO','MARCA')       
    computadora2 = Computadora('KYCERA',monitor2,ratón2,teclado2)
    print(computadora2)
