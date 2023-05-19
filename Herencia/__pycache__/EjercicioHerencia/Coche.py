from EjercicioHerencia import Vehículo

class Coche(Vehículo):

    def __init__(self, velocidad, color, ruedas):
        super().__init__(color,ruedas)
        self.velocidad = int(velocidad)
    
    def __str__(self) -> str:
        return f'Característica: {super().__str__()} Velocidad: {self.velocidad}'

Coche1 = Coche(70,'Azul',120)
print(Coche1)