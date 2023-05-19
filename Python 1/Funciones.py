def miFuncion():
    print('Hola mundo')

miFuncion()

def Suma (num1,num2):
    return num1 + num2
print(Suma(2,2))

def Practica():
    print('HOLA MUNDO')
Practica()

#Llamar varios valores *args = argumentos

def ListaNombres(*args):
    for nombres in args:
        print(nombres)
ListaNombres('Steeven','David','Rodríguez','Zhunio')

#EJERCICIO 
'''
Crear una funcion para sumar los valores recibidos de tipo numérico,utilizando
argumentos variable * args como parámetro de la función y regresar como resultado
la suma de todos los valores pasados como argumentos
'''

def numéricos(*args):
    suma = 1
    for numeros in args:
        suma *=numeros
    print(f'Valor total:{suma}')
numéricos(2,2,2)
#Iterar una lista o Nombre 
def DesplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)
ListaNom=['Steeven','David','Rodriguez','Zhunio']
DesplegarNombres(ListaNom)
DesplegarNombres('Steeven')

#EJERCICIO DE NUMERO FACTORIAL
'''Funciones recursiva'''
def Factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * Factorial(numero-1)
resultado = Factorial(5)
print(f'Numero Factorial:{resultado}')


#EJERCICIO DE FUNCION RECURSIVA PERO RESTANDO UN NUMERO
def Descende(numero):
    if numero >=5:
        print(numero)
        return Descende(numero-1)
    elif numero==1:
        return
    elif numero < 0:
        print('Valor incorrecto')

# CONVERTIR DE GRADOS C A F Y AL CONTRARIO 

def Celsius(valor):
    f = valor*1.8+32
    print(f'Grado C a F es:{f}')

Celsius(2)

def Fahrenheit(valor):
    c = (valor-32)/1.8
    print(f'El valor de Fahrenheit es: {c}')

Fahrenheit(2.2)
'''
def Numero(*args):
    Numero = 1
    for Mul in args:
        Numero*=Mul
    print(Numero)
Numero(5,4,3,2,1)
'''
