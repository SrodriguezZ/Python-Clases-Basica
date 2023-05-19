class Persona:

    contador_personas  = 0
    @classmethod
    def Generar_Contador(cls):
        cls.contador_personas +=1
        return
    def __init__(self, nombre, apellido) -> None:
        self.id_contador = Persona.Generar_Contador()
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self) -> str:
        return f'Id_Persona[{self.id_contador}]{self.nombre} {self.apellido}'
    

persona1= Persona('Steeven','Rodríguez')
print(persona1)
persona2= Persona('Saira','Zhunio')
print(persona2)
persona3= Persona('Joanna','Pardo')
print(persona3)
print(f'Contador de Persona[{Persona.contador_personas}]')