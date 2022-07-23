#LOGICAL OPERATORS
# a == b IGUAL QUE
# a < b MENOR QUE
# a > b MAYOR QUE
# a != b DIFERENTE DE
# a <= b MENOR IGUAL QUE
# a >= b MAYOR IGUAL QUE

# CONDITIONAL SENTENCE "IF"
if 2 == 2:
    print('2 es igual a 2')
if 6 > 4:
    print('6 es mayor que 4')
if 4 < 6:
    print('3 es menor que 6')
if 1 != 2:
    print('1 es distinto a 2')
if 4 <= 6 :
    print('4 es menor o igual a 6')
if 1 >= 1 :
    print('1 es mayor o igual a 1')

if 2 > 5:
    print('incorrecto')
elif 2 < 5:
    print('2 es menor que 5 en elif')
else:
    print('imprimo si todo lo anterior es falso')

# IF CORTO
if 3 < 6: print('if en una linea')

# IF ELSE CORTO
print('cuando devuelve true') if 3 > 6 else print('cuando devuelve false')

# AND : ambas condiciones deben ser true.
if 3 < 6 and 3 > 1:
    print('ambas son true')
if 3 < 6 and 3 < 1:
    print('hay una falsa, esto no se mostrara')

# OR : si una condición evalua en true se ejecuta la instrucción.
if 1 < 0 or 1 > 0:
    print('una de las dos es true')
# OR : si ambas condiciones son falsas no se ejecuta.
if 1 < 0 or 1 < 0:
    print('si ambas son false no se ejecuta')