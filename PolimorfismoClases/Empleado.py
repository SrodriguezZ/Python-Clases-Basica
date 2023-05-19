class Empleado:

    def __init__(self, nombre, sueldo) -> None:
        self.nombre = nombre
        self.sueldo = sueldo
    def __str__(self) -> str:
        return f'Nombre:[{self.nombre}] Sueldo:[{self.sueldo}]'
    
