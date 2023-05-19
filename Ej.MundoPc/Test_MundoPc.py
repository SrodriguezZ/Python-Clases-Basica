from Computadora import Computadora
from Monitor import Monitor
from Ratón import Ratón
from Teclado import Teclado
from Orden import Orden



monitor1 = Monitor('LG','900')
ratón1 = Ratón('USB','DELL')
teclado1 = Teclado('USB','MARCA')       
computadora1 = Computadora('RICOH',monitor1,ratón1,teclado1)

monitor2 = Monitor('ACER','1000')
ratón2 = Ratón('USB','HP')
teclado2 = Teclado('INALÁMBRICO','MARCA')       
computadora2 = Computadora('KYCERA',monitor2,ratón2,teclado2)

Computadoras1 =[computadora1, computadora2]
orden1 = Orden(Computadoras1)
orden1.Agregar_Computadora(computadora2)
print(orden1)
print('SEPARADOR'.center(50,'-'))
monitor3 = Monitor('LG','900')
ratón3 = Ratón('USB','DELL')
teclado3 = Teclado('USB','MARCA')       
computadora3 = Computadora('GAMER',monitor3,ratón3,teclado3)

monitor4 = Monitor('ACER','1000')
ratón4 = Ratón('USB','HP')
teclado4 = Teclado('INALÁMBRICO','MARCA')       
computadoras4 = Computadora('KYCERA',monitor4,ratón4,teclado4)
Computadoras2 = [computadora3,computadoras4]
orden2 = Orden(Computadoras2)
orden2.Agregar_Computadora(computadoras4)
print(orden2)

print('SEPARADOR'.center(50,'-'))


