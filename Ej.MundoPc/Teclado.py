from DispositoEntrada import DispositivoEntrada as Dis
class Teclado(Dis):

    contador_teclado = 0
    @classmethod
    def Contador_Teclado(cls):
        cls.contador_teclado+=1
        return cls.contador_teclado
    
    def __init__(self,tipo_entrada, marca) -> None:
        super().__init__(tipo_entrada,marca)
        self._id_teclado = Teclado.Contador_Teclado()
    
    def __str__(self) -> str:
        return f'ID_TECLADO:[{self._id_teclado}][{super().__str__()}]'
    
if __name__=='__main__':
    teclado = Teclado('USB','MARCA')
    print(teclado)
    teclado2= Teclado('INALÁMBRICO','HP')
    print(teclado2)