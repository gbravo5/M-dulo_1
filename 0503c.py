# entrada de datos
nb_a = input('¿introduzca un número entero?: ')

isvalid0 = False
while not isvalid0:
    if nb_a[1:].isdigit():
        nb_a = int(nb_a)
        isvalid0 = True
    else:
        print(nb_a, 'debe ser un número entero')
        nb_a = input('¿introduzca un número entero?: ')

nb_b = input('¿introduzca otro número entero?: ')
isvalid1 = False
while not isvalid1:
    if nb_b[1:].isdigit():
        nb_b = int(nb_b)
        isvalid1 = True
    else:
        print(nb_b, 'debe ser un número entero')
        nb_b = input('¿introduzca un número entero?: ')
        
# procesamiento datos

nb_a = nb_a/10
nb_b = nb_b/10

add      = round(nb_a + nb_b, 2)
subtract = round(nb_a - nb_b, 2)
multiply = round(nb_a * nb_b, 2)
divide   = round(nb_a / nb_b, 2)

# salida resultados
print(nb_a, '+', nb_b, '=', add)
print(nb_a, '-', nb_b, '=', subtract)
print(nb_a, '*', nb_b, '=', multiply)
print(nb_a, '/', nb_b, '=', divide)