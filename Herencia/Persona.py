class Persona:

    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self) -> str:
        return f'Nombre:{self.nombre} Edad:{self.edad}'


class Empleado(Persona):
    def __init__(self,nombre,edad, sueldo):
        super().__init__(nombre,edad)
        self.sueldo = sueldo
    
    def __str__(self) -> str:
        return f'EMPLEADO:{super().__str__()} {self.sueldo}'


if __name__ == '__main__':   
    empleado1 = Empleado('Steeven',27,450)
    print(empleado1.nombre)