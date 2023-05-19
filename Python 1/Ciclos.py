#CICLO WHILE
Numero = 0
while Numero<10:
    Numero+=1
    print(Numero)
else:
    print('Paso')
#MANERA DESCENDENTE
Desc = 5
while Desc>=1:
    print(Desc)
    Desc -=1
else:
    print('paso')

#CICLO FOR
'''Break: Ayuda a romper el ciclo'''
'''Continue: Continua la siguiente interacción'''
# FOR 
cadena  = 'HOLA'
for letra in cadena:
    print(letra)
else: 
    print('FIN')

letra = 'España'
for Palabra in letra:
    if Palabra == 'a':
        print(f'Palabra encontrada: {Palabra}')
        break
else:
    print('Fin del ciclo')

Numero = 1
for Numero in range(6):
    if Numero % 2!=0:
        continue
        print(Numero)

