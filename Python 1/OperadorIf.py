#Ejercicio con el if 

'''''Mes = int(input('Ingrese el mes del año(1-12): '))
estación = None
if Mes == 1 or Mes == 2 or Mes ==12:
    estación = 'Invierno'
elif Mes == 3 or Mes == 4 or Mes ==5:
    estación = 'Primavera'
elif Mes == 6 or Mes == 7 or Mes== 8:
    estación = 'Verano'
elif Mes == 9 or Mes == 10 or Mes ==11:
    estación = 'Otoño'
else:
    print('MES INCORRECTO')
print(f'Para el mes {Mes} la estación es: {estación}')'''
''

#PROPORCIONA TU EDAD

'''Edad = int(input('Proporciona tu edad: '))
x = None
if  0 <= Edad < 10:
    x = 'La infancia es increíble'
elif 10 <= Edad <20:
    x = 'Mucho cambios y mucho estudio'
elif 20<= Edad <=30:
    x = 'Amor y comienza el trabajo'
else: 
    print('Etapa de vida no reconocida')
print(f'EDAD: {Edad} --- {x}')'''

#INSTRUCCIÓN DE LA TAREA
Usuario = int(input('Ingrese la nota: '))
Mensaje = None
if 9<=Usuario<10:
    Mensaje='A'
elif 8<=Usuario<9:
    Mensaje='B'
elif 7<=Usuario<6:
    Mensaje='D'
elif 0<=Usuario<=6:
    Mensaje='F'
else:
    print('Valor Incorrecto')
print(Mensaje)
