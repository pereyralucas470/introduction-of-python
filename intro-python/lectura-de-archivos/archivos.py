# a = open('archivoTexto.txt', 'w')
# a.write('\nagregar linea de texto')
# a.close()

# c = open('archivoTexto.txt')
# print(c.read())

import os

if os.path.exists('archivoTexto.txt'): 
    os.remove('archivoTexto.txt')       #ELIMINAR ARCHIVO
else:
    print('el archivo no existe')

os.rmdir('micarpeta')                   #ELIMINAR CARPETA