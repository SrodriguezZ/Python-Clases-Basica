
class Vehículo:

    def __init__(self,color,ruedas) -> None:
        self.color = color
        self.ruedas = ruedas

    def __str__(self) -> str:
        return 'Color:' + self.color + 'Rueda:'+ str(self.ruedas)
    
class Coche(Vehículo):

    def __init__(self, color, ruedas, velocidad) -> None:
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self) -> str:
        return 'Característica:' + super().__str__() + 'Velocidad:' + str(self.velocidad)
    
class Bicicleta(Vehículo):

    def __init__(self, color, ruedas, bicicleta) -> None:
        super().__init__(color, ruedas)
        self.bicicleta = str(bicicleta)
    def __str__(self) -> str:
        return f'Característica: {super().__str__()} Tipo: {self.bicicleta}'