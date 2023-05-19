from Cuadrado import Cuadrado
from Rectangulo import Rectángulo

print('Creación de Objeto Cuadrado'.center(50,'-'))

Cuadrado1 = Cuadrado(lado=5,color='Blanco')
Cuadrado1.alto = -10
print(f'Calculo del Cuadrado: {Cuadrado1.CalculoArea()}')


print('Creación de Objeto Rectángulo'.center(50,'-'))
Rectángulo1 = Rectángulo(6,6,'Negro')
print(f'Calculo del Rectángulo:{Rectángulo1.CalcularArea1()}')