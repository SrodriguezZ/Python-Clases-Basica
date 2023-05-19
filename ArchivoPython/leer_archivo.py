#archivo = open('c:\\CARPETA\\ARCHIVO\\prueba.txt','r')
archivo = open('prueba.txt','r',encoding='utf8')

'IMPRIMIR ENTRE CARACTERES'
#print(archivo.read(4))
'IMPRIMIR ENTRE LINEAS'
#print(archivo.readline())
'IMPRIMIR TODO'
#print(archivo.read())
'ITERAR EL ARCHIVO'
#for lineas in archivo:
#    print(lineas)
'leer lineas de una lista'
#print(archivo.readlines())
'acceder a una linea de la lista'
#print(archivo.readlines()[0])    
'copiando a otro archivo'
archivo2 = open('copia.txt','w',encoding='utf8')
archivo2.write(archivo.read())

archivo.close()
archivo2.close()