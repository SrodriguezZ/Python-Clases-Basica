from NumerosIdenticoException import NumerosIdénticos
Resultado = None

try:
    a = int(input('Primer numero: '))
    b = int(input('Segundo numero:  '))
    if a == b:
        raise NumerosIdénticos('HOLA EXCEPTION')
    resultado = a/b
except Exception as e:
    print(f'OCURRIO UN ERROR:{e}')
else:
    print('No ocurrió ningún error')
finally:
    print('Ejecución finally')
print(f'RESULTADO:{Resultado}')