#-----LISTA-------

lista = ['hola','Mundo','Steeven','Rodríguez']
print(type(lista))
print(lista[2:4])
#MANERA INVERSA
print(lista[-1])
#ir de inicio de la lista al indice(sin incluirlo)
print(lista[:3])
#Desde el indice indicado hasta el final
print(lista[1:])
#cambiar indice
lista[3]='Zhunio'
print(lista)
#Interactuar Lista
for Lista in lista:
    print(Lista)
#preguntar el largo de una lista
print(len(lista))
#insertar un elemento en la lista
lista.append('Kyra')
print(lista)
#agregar un elemento asignado
lista.insert(1,'Ecuador')
#Remover un elemento 
lista.remove('Kyra')
print(Lista)
#eliminar un indice
del lista[2]
print(lista)
'''
#borrar los elementos de la lista
lista.clear()
print(lista)
#borrar
del lista()
print(lista)
''' 
#---TUPLE----INMUTABLE 
frutas = ('Manzana','Pera','Uva','Plátano','Arándanos')
#saber lo largo
print(len(frutas))
#acceder a los elementos 
print(frutas[1:])
#acceder a la inversa
print(frutas[-1])
#aplicando un for
for i in frutas:
    print(i, end=' ')#Aplicando end para evitar salto de lineas 
#Cambiar valores en una tuple
lista_frutas = list(frutas)
lista_frutas[0]='Frutilla'
fruta = tuple(lista_frutas)
print('\n',lista_frutas)
#EJERCICIO DE TUPLE - CREAR UNA LISTA QUE SOLO INCLUYA LOS NÚMEROS MENOS A 5
tuple = (13,1,8,3,2,5,8)
lista = list(tuple)
n = []
for numero in lista:
    if numero <5:
        n.append(numero)
print(n)

#---SET---No mantiene un orden

se_t={'Lunes','Martes','Miércoles','Jueves','Viernes'}
print(type(se_t))
print(se_t)
#Largo de los elementos
print(len(se_t))
#revisar si un elemento esta presente
print('Martes'in se_t)
#agregar elementos 
se_t.add('Sábado')
print(se_t)
#eliminar elementos
se_t.remove('Sábado')
print (se_t)
'''#eliminar 
se_t.clear()
print(se_t)'''

#---DICCIONARIO---
Lenguaje = {
    'Python':'SQL',
    'Java':'Django',
    'PHP':'Html'
}
print(Lenguaje)
#ver llave
print (Lenguaje.keys())
#ver resultado
print(Lenguaje['Python'])
#ver clave todas
print(Lenguaje.values())
# ver una especificado
print(Lenguaje.get('Python'))
#modificar elementos
Lenguaje['Python']='Postgres'
print(Lenguaje)
#recorrer los elementos
for termino, valor in Lenguaje.items():
    print(termino, valor)
# llave
for termino in Lenguaje.keys():
    print(termino)
#valor
for valor in Lenguaje.values():
    print(valor)
#comprobar una existencia
print('Python' in Lenguaje)
#Agregar 
Lenguaje['hola']='Mundo'
print(Lenguaje)
#eliminar
Lenguaje.pop('hola')
print(Lenguaje)
