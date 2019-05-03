#for, opción corta y SIN tratamiento excepciones -------#

def longitud(tupla):
    return len(tupla)
    
notas = (2, 4, 6, 8)

sum = 0
count = 0
for i in range(0, longitud(notas)):
    sum += notas[i]
    count += 1
    avg = sum / count
print('nb_notas: ', count)
print('total_notas: ', sum)
print('nota_media: ', avg)
