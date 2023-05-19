#Ejercicio de Par O Impar
'''Numero = int(input('Ingrese un numero: '))

if Numero%2==0:
    print('NUMERO PAR')
else:
    print('NUMERO IMPAR|')'''

#Ejercicio de mayor
'''Edad = int(input('Ingrese la edad: '))

if Edad>=18:
    print(f'Mayor de edad: {Edad}')
else:
    print(f'Menor de edad: {Edad}')
'''
# OPERADOR LÓGICO 
#AND
'''x = int(input('Ingrese un numero 0 al 5: '))
if x >=0 and x<=5:
    print(f'Dentro del rango: {x}')
else:
    print(f'Fuera del rango: {x}')'''
#OR
'''Vacaciones =  False
Descanso = False
if Vacaciones or Descanso:
    print('SI PUEDE ASISTIR')
else:
    print('NO PUEDE ASISTIR ')
edad = int(input('Ingrese la edad: '))
if  (20<= edad <30) or (30<= edad <40):
    print('DENTRO DE LOS 20 Y 30')
else:
    print('FUERA DE RANGO')'''

#Ejercicio de mayo de dos numeros

'''Numero1 = int(input('Ingrese Numero: '))
Numero2 = int(input('Ingrese Numero2: '))
if Numero1>Numero2:
    print(f'Numero1 es mayor: {Numero1}')
else:
    print(f'Numero2 es mayor: {Numero2}')'''

#Tienda de Libros 
Libro = input('Proporcione el nombre del libro: ')
id = int(input('Ingrese el id del libro: '))
Precio = float(input('Ingrese el precio del libro: '))
Envío = input('Indique si es envío gratuito (True/False): ')
if Envío=='True':
    Envío = True
elif Envío=='False':
    Envío= False
else:
    print('No ingrese bien el comentario')

print(f'''
    Nombre: {Libro}
    ID: {id}
    Precio = {Precio}
    Envío = {Envío}
''')
