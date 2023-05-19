try:
    archivo = open('prueba.txt','w',encoding='utf8')
    archivo.write('HOLA CÓMO ESTAS\n')
    archivo.write('ADIOS')
except Exception as e:
    print(e)
finally:
    archivo.close()
