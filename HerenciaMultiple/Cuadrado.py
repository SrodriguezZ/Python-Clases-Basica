
from Color import Color
from FiguraGeometrica import FiguraGeométrica


class Cuadrado(FiguraGeométrica, Color):
    
    def __init__(self, lado, color) -> None:
        FiguraGeométrica.__init__(self, lado, lado)
        Color.__init__(self, color)
    
    def Calcular_Area(self):
        return self.alto * self.ancho