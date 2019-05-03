def esDecimalPositivo(nb_str):
    try:
        float(nb_str)
        if float(nb_str) < 0:
            return False
        else:
            return True
    except ValueError:
        return False


def valid(mensaje):
    nb_str = input(mensaje)
    while not esDecimalPositivo(nb_str):
        print(nb_str, 'Debe ser un número positivo')
        nb_str = input(mensaje)
    return nb_str
    

base_str = valid('Base del Triángulo: ')
altura_str = valid('Altura del Triángulo: ')

base = float(base_str)
altura = float(altura_str)

area = base * altura / 2

print('El Área del Triángulo es: ', round(area, 2))