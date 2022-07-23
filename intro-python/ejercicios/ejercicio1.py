#multiplicar dos numeros sin usar el simbolo de multiplicacion
from wsgiref.validate import InputWrapper
from xmlrpc.client import boolean


n1 = 4
n2 = 8
resultado = 0

for x in range(n1):
    resultado +=n2

print(resultado)

# ingresar nombre y apellido e imprimirlo al reves
nombre = 'Lucas'
apellido = 'Pereyra'

concatenacion = nombre + ' ' + apellido

print(concatenacion[::-1])


# escribir una funcion que encuentre el elemento menor de una lista
lista = [1, 2, 5, 3, 55, -24, -13]

menor = 'init'

for x in lista:
    if menor == 'init':
        menor = x
    else:
        menor = x if x < menor else menor

print('menor', menor)

#escribir una funcion que devuelva el volumen de una esfera por su radio
# 4/3 * pi * r ** 3
def calcularVolumen(r):
    return 4/3 * 3.14 * r ** 3
    
resultado = calcularVolumen(6)
print(resultado)    

# escribir una funcion que indique si el usuario es mayor de edad
def mayorEdad(usuario):
    return usuario.edad > 17

class Usuario:
    def __init__(self, edad):
        self.edad = edad

usuario = Usuario(16)
usuario2 = Usuario(22)

resultado1 = mayorEdad(usuario)
resultado2 = mayorEdad(usuario2)

print(resultado1, resultado2)

# escribir una funcion que indique si un numero es par o impar
def esPar(n):
    return n % 2 == 0

resultado = esPar(10)
print(resultado)

# escribir una funcion que indique cuantas vocales tiene una palabra
palabra = 'PalAbra'
vocales = 0

for x in palabra:
    y = x.lower()
    vocales += 1 if y == 'a' or y == 'e' or y == 'i' or y == 'o' or y == 'u' else 0

print(vocales)    

# escribir una aplicacion que reciba una cantidad infinita de numeros hasta
# decir basta, luego que devuelva la suma de los numeros ingresados

# lista = []
# print('Ingrese numeros y para salir escriba "basta"')

# while True:
#     valor = input('Ingrese valor: ')
#     if valor == 'basta':
#         break
#     else:
#         try:
#             valor = int(valor)
#             lista.append(valor)
#         except:
#             print('Dato invalido')
#             exit()

# resultado = 0

# for x in lista:
#     resultado += x

# print(resultado)

# escribir una funcion que reciba nombre y apellido y los vaya agregado
# a un archivo

def agregaNombreAArchivo(nombre, apellido):
    c = open('nombrecompleto.txt', 'a')
    c.write(nombre + ' ' + apellido + '\n')
    c.close()

agregaNombreAArchivo('Lucas', 'Pereyra')
