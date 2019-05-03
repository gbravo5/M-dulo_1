def validacion(mensaje):
    nb = input(mensaje)
    isvalid0 = False
    while not isvalid0:
        if nb[1:].isdigit():
            nb = int(nb)
            isvalid0 = True
        else:
            print(nb, 'debe ser un número entero')
            nb = input(mensaje)

    return nb

nb_a = validacion('introduzca un número entero: ')
nb_b = validacion('introduzca otro número entero: ')

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