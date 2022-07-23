def miFuncion():
    print('Mi primera funcion en Python')

# miFuncion()

# def imprimirDato(nombre, apellido):
#     print('El nombre completo es:', nombre, apellido)

# imprimirDato('Lucas', 'Pereyra')

def imprimirDato(*nombre):
    print('El nombre completo es:', nombre[1])

# imprimirDato('Name1', 'Name2')

def nombreCompleto(apellido, nombre):
    print(nombre, apellido)

# nombreCompleto(nombre='Name', apellido='Lastname')

def nombreCompleto2(**kwargs):
    print(kwargs['nombre'], kwargs['apellido'])

# nombreCompleto2(nombre='Name', apellido='Lastname')

def recursion(i):
    if(i < 1):
        return i
    print(i)
    recursion(i - 1)

recursion(5)