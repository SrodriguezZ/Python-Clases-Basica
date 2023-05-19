import re
mensaje = 'Hola mundo como están'
x = re.split(' ',mensaje)
for letra in x: 
    print(letra)

lista = [i for i in range(1, 1000+1) if i%2!=0]
print(lista)