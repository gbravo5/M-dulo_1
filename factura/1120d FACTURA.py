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

cantidad_str = valid('Introduzca la Cantidad: ')
precio_str   = valid('Introduzca el Precio Unitario (eur): ')

cantidad     = float(cantidad_str)
precio       = float(precio_str)

total_unidades = 0   
total_fra   = 0

desglose_fra  = []   
_UNIDADES = 0
_EUR = 1
_COSTE = 2

while cantidad > 0 and precio > 0:
    
    total_coste = cantidad * precio
    desglose_fra.append([cantidad, precio, total_coste]) 
    
    total_unidades += cantidad
    total_fra      += total_coste
    
    cantidad_str = valid('Introduzca la Cantidad: ')
    cantidad     = float(cantidad_str)
    if cantidad == 0:
        continue
    else:
        precio_str   = valid('Introduzca el Precio Unitario (eur): ')
        precio       = float(precio_str)
  
for item in desglose_fra:
    
    if item[_UNIDADES] <= 1:
        unidad_txt = 'unidad'
    else:
        unidad_txt = 'unidades'
        
    print ('\n' + '%.2f %s - ' %(item[_UNIDADES], unidad_txt) + '%.2f eur/unidad - ' %(item[_EUR]) + 'total coste %.2f' %(item[_COSTE]))
        
print('---------------------------------------------------------------------------')
print('Total Factura (eur): %.2f\n' %(total_fra) + 'Total Unidades: %.2f' %(total_unidades))