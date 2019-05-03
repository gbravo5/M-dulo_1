mytxt = 'En    un lugar de la Mancha, de cuyo nombre no quiero acordarme, no ha mucho tiempo que vivía un hidalgo de los de lanza en astillero, adarga antigua, rocín flaco y galgo corredor.'\
        'Una olla de algo más vaca     que carnero, salpicón las más noches, duelos y quebrantos los sábados, lantejas los viernes, algún palomino de añadidura los domingos, consumían las tres partes de su hacienda.'\
        'El resto della concluían      sayo de velarte, calzas de velludo para las fiestas, con sus pantuflos de lo mesmo, y los días de entresemana se honraba con su vellorí de lo más fino.'\
        'Tenía en su casa una ama que pasaba de los cuarenta, y una sobrina que no llegaba a los veinte, y un mozo de campo y plaza, que así ensillaba el rocín como tomaba la podadera.'\
        'Frisaba     la edad de nuestro hidalgo con los cincuenta años; era de complexión recia, seco de carnes, enjuto de rostro, gran madrugador y amigo de la caza.'\
        'Quieren decir que tenía el sobrenombre de Quijada, o Quesada, que en esto hay alguna diferencia en los autores que deste caso escriben; aunque por conjeturas verosímiles se deja entender que se llamaba Quijana.'\
        'Pero esto      importa poco a nuestro cuento: basta que en la narración dél no se salga un punto de la verdad.      '

def exists(character, list_character):
    # la función recorre la lista y si encuentra el carácter, devolverá su posición
    index = 0
    while index < len(list_character):
        if list_character[index] == character:
            return index 
        index += 1
    # si tras recorrer la totalidad de la lista (while stop) no encuentra el carácter, devolverá su None
    return None

list_character = []
list_frequency = []

for character in mytxt:
    i = exists(character, list_character)
    if i != None:
        list_frequency[i] +=1
    else:
        # para la primera vez que aparezca
        list_character.append(character)
        list_frequency.append(1)
        
print(list_character)
print(list_frequency)


# opción 1
index = 0
while index < len(list_character):
    print(list_character[index], '-', list_frequency[index])
    index += 1

# opción 2
dict = {}
for i, j in zip(list_character, list_frequency):
    dict[i] = j
print(dict)