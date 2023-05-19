
class FiguraGeometrica:

    def __init__(self, alto, ancho) -> None:
        if self._Validar_Valor(alto):
         self._alto = alto
        else:
           self._alto =0
        if self._Validar_Valor(ancho):
         self._ancho = ancho
        else:
           self._ancho = 0

    @property
    def alto(self):
        return self._alto
    @alto.setter
    def alto(self,alto):
        if self._Validar_Valor(alto):
         self._alto = alto
        else:
           print(f'Valor erróneo de alto:{alto}')
    
    @property
    def ancho(self):
        return self._ancho
    @ancho.setter
    def ancho(self,ancho):
        if self._Validar_Valor(ancho):
         self._ancho=ancho
        else:
           print(f'Valor Erróneo:{ancho}')

    def __str__(self) -> str:
        return f'Alto: {self._alto} Ancho_ {self._ancho} '
    
    def _Validar_Valor(self,valor):
       return True if 0<valor<10 else False 


