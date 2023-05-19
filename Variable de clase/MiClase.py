class MiClase:

    variable_clase='valor variable clase'

    def __init__(self,variable_instancia) -> None:
        self.varibale_instancia = variable_instancia

    @staticmethod
    def metodo_estatico():
        print(MiClase.variable_clase)

    @classmethod
    def metodo(cls):
        print(cls.variable_clase)

        
print(MiClase.variable_clase)
miclase = MiClase('Variable de Instancia')
print(miclase.varibale_instancia)

#Creacion de una variable al vuelo
MiClase.variable_clase2 = 'Variable de Clase2'
print(MiClase.variable_clase2) 
miclase.metodo()