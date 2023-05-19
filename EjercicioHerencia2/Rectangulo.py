from FiguraGeometrica import FiguraGeometrica
from Color import Color

class Rectángulo(FiguraGeometrica,Color):

    def __init__(self, alto, ancho, color) -> None:
        FiguraGeometrica.__init__(self,alto,ancho)
        Color.__init__(self,color)
    
    def CalcularArea1(self):
        return self.alto*self.ancho
    
    def __str__(self) -> str:
        return f'Rectángulo: {FiguraGeometrica.__str__(self)}Color: {Color.__str__(self)}'
    


