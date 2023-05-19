from FiguraGeometrica import FiguraGeometrica
from Color import Color

class Cuadrado(FiguraGeometrica, Color):

    def __init__(self, lado, color) -> None:
        FiguraGeometrica.__init__(self,lado,lado)
        Color.__init__(self,color)

    def CalculoArea(self):
        return self.alto*self.ancho

    def __str__(self) -> str:
        return f'Resultado del Area:{FiguraGeometrica.__str__(self)} Color: {Color.__str__(self)}'

    
