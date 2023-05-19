
class Vehículo:

    def __init__(self, color, ruedas) -> None:
        self.color = str(color)
        self.ruedas = int(ruedas)
    
    def __str__(self) -> str:
        return f' Color:{self.color} Rueda: {self.ruedas}'
    
veh = Vehículo('Azul',60)
print(veh)