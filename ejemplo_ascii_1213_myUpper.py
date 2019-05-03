str = 'HOLA'
for i in str:
    print(i, '-', ord(i))

str = 'hola'
for i in str:
    print(i, '-', ord(i))


def myUpper(str):
    result = ''             # acumulador
    for i in str:
        j = ord(i) - 32           # código ascii del str, pero el relativo a su versión en mayúsculas (gap min/may -32)
        if j >= 97 and j <= 122:  # excluimos de la transformación códigos ascii donde no aplique (espacio en blanco, por ejemplo)
            result += chr(j)      # transformo ascii código caracter mayúsculas en el caracter en mayúsculas correspondiente
        else:
            result += i
    return result   

saludo = input('saluda:')
print(myUpper(saludo))

# 32-127 códigos ascii predefinidos y fijos