from Empleado import Empleado
class Gerente(Empleado):
    
    def __init__(self, nombre, sueldo, departamento) -> None:
        super().__init__(nombre, sueldo)
        self._departamento = departamento

    def __str__(self) -> str:
        return f'GERENTE[Departamento:{self._departamento}]{super().__str__()}'