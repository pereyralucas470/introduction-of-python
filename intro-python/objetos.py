class Usuario: # SIEMPRE PRIMER LETRA MAYUSCULA EN CLASES
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    
    def saludo(self):
        print('Hola, mi nombre es', self.nombre, self.apellido)    

class Admin(Usuario):
    def saludoAdmin(self):
        print('Hola, me llamo', self.nombre, ' y soy administrador')

# usuario = Usuario('UserNombre', 'UserApellido')
# admin = Admin('AdminNombre', 'AdminApellido')

# usuario.saludo()
# admin.saludo()
# admin.saludoAdmin()

# EJERCICIO HERENCIA
class Animal():
    def __init__(self, nombre, onomatopeya):
        self.nombre = nombre
        self.onomatopeya = onomatopeya
    
    def saludo(self):
        print('Hola, soy un', self.tipo, 'y mi sonido es el', self.onomatopeya)

class Gato(Animal):
    tipo = 'gato'

class Perro(Animal):
    tipo = 'perro'

class Vaca(Animal):
    tipo = 'vaca'

gato = Gato('Gato1', 'maullido')
gato.saludo()

perro = Perro('Perro1', 'ladrido')
perro.saludo()

vaca = Vaca('Vaca1', 'mugido')
vaca.saludo()
