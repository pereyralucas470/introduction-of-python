#BASIC MATHEMATICS
# + Addition
# - Subtraction
# * Multiplication
# / Division

# VARIABLES AND MULTIPLE VARIABLES
my_name, age, nationality = 'Lucas', 19, 'Argentina'
email = 'lucaspereyra470@gmail.com'

print(my_name, age, nationality)
print(email)

# CONCATENATION
start = 'Hello '
final = 'world'

print(start + final)

# STRING AND NUMBERS
word = 'hello world' # string
phrase = "hello world with double quotes" # string

wholeNumber = 20 # integer
decimalNumber = 20.2 # float
complexNumber = 1j

print(word, phrase, wholeNumber, decimalNumber, complexNumber)

# LISTS
lista = ['Hi', 'Hola', 'Oi']
lista2 = lista.copy()
lista.append('Hello')
#lista.clear()

print(lista, lista2.count('Hi'))
print(len(lista), len(lista2)) #longitud
print(lista[2]) #positions

#lista.pop() # delete last element
#lista.remove(4) # delete element you want
lista.reverse()
lista.sort()

tupla = ('hi', 'world', 'i am', 'tupla')
listaDeTupla = list(tupla)
listaDeTupla.append('1')
print(listaDeTupla)

# RANGE
rango = range(6)
#print(rango)

# DICCIONARIO
diccionario = {
    "nombre": "Lucas",
    "edad": 19
}
#print(diccionario)
#print(diccionario['edad'])
#print(diccionario.get('nombre'))
diccionario['nombre'] = 'Samuel'
print(diccionario)
print(len(diccionario))

diccionario['mayor de edad'] = 'SI'
print(diccionario)
#diccionario.pop('mayor de edad')
#diccionario.popitem()
del diccionario['mayor de edad']
print(diccionario)

lucas = {
    "nombre": "Lucas",
    "edad": 19
}
samuel = {
    "nombre": "Samuel",
    "edad": 19
}

#diccionarioAnidado = {
#    "Lucas": {
#        "nombre": "Lucas",
#        "edad": 19
#    },
#    "Samuel": {
#        "nombre": "Samuel",
#        "edad": 19
#    }
#}

diccionarioAnidado = {
    "Lucas": lucas,
    "Samuel": samuel
}

print(diccionarioAnidado)

alumno = dict(nombre="Lucas Samuel")
print(alumno)