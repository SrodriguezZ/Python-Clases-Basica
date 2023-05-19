class  Persona:

    def __init__(self, nombre, apellido, edad ) -> None:
        self._nombre = nombre
        self.apellido = apellido
        self.edad = edad
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre
    
    def mostrar_detalle(self):
        print(f'Persona: {self._nombre} {self.apellido} {self.edad}')

if __name__ in '__main__': 
    persona1 = Persona('Steeven','Rodríguez',27)
    print(persona1.nombre)
    persona1.nombre = 'David'
    print(persona1.nombre)
