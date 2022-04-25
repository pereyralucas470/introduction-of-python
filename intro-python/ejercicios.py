# dato = input('Ingrese un dato: ')

# lista = ['hola', 'mundo', 'dragon', 'perro']

# if lista.count(dato) > 0:
#     print('El dato existe:', dato)
# else:
#     print('El dato no existe.')

# CALCULADORA
numero1 = input('Ingrese primer número: ')
try:
    numero1 = int(numero1)
except:
    numero1 = 'error'

if numero1 == 'error':
    print('Ingresaste mal los datos.')
    exit()

numero2 = input('Ingrese segundo número: ')
try:
    numero2 = int(numero2)
except:
    numero2 = 'error'

if numero2 == 'error':
    print('Ingresaste mal los datos.')
    exit()    

simbolo = input('Ingrese operación: ')
if simbolo == '+':
    print(numero1 + numero2)
elif simbolo == '-':
    print(numero1 - numero2)
elif simbolo == '*':
    print(numero1 * numero2)
elif simbolo == '/':
    print(numero1 / numero2)
else:
    print('El simbolo ingresado no es válido.')


