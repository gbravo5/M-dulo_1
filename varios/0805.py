#for, opción larga y CON tratamiento excepciones -------#

# tratamiento excepciones:
def contenido(tupla, indice):
    try:
        result = tupla[indice]
    except:
        result = None
    
    return result

# definición longitud:
def longitud(tupla):
    indice = 0
    while contenido(tupla, indice) != None:
        indice += 1
    return indice
    

notas = (2, 4, 6, 8)

suma = 0
for i in range(0, len(notas)):
    suma += notas[i]

avg = suma / len(notas)

print('nb_notas...: ', len(notas))
print('total_notas: ', suma)
print('nota_media.: ', avg)