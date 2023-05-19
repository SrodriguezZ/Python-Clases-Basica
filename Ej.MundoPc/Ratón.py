from DispositoEntrada import DispositivoEntrada as Dis
class Ratón(Dis):

    contador_ratón = 0
    @classmethod
    def Contador(cls):
        cls.contador_ratón +=1
        return cls.contador_ratón
    
    def __init__(self, tipo_entrada, marca) -> None:
        super().__init__(tipo_entrada, marca)
        self.id_ratón = Ratón.Contador()
    
    def __str__(self) -> str:
        return f'ID_RATÓN:[{self.id_ratón}]{super().__str__()}'
if __name__=='__main__':    
    ratón1 = Ratón('USB','DELL')
    print(ratón1)
    ratón2 = Ratón('INALÁMBRICO','HP')
    print(ratón2)
    
