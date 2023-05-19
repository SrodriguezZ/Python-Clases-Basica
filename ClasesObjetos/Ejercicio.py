class Aritmética:
    
    def __init__(self, OperandoA, OperandoB) -> None:
        self.operandoA = OperandoA
        self.operandoB = OperandoB
    
    def sumar(self):
        return self.operandoA + self.operandoB
    
    def restar(self):
        return self.operandoA - self.operandoB
    
    def división(self):
        return self.operandoA/self.operandoB

    
aritmética = Aritmética(5,3)
print(f'Suma: {aritmética.sumar()}')
print(f'Restar: {aritmética.restar()}')
print(f'División:{aritmética.división():.2f}')#:.2f numero flotante

class Rectángulo:

    def __init__(self,Base,Altura) -> None:
        self.base = Base
        self.altura = Altura
    
    def Calculo(self):
        return self.base * self.altura

Base = int(input('Proporciona la base: '))
Altura = int(input('Proporciona la altura: '))
medida = Rectángulo(Base,Altura)
print(f'Área rectángulo: {medida.Calculo()}')