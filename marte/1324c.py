# identifican el mensaje como una serie númerica de grados en base 16 (360 grados / 16 = 22.5)
degree_message = [90, 180, 135, 337.50, 135, 270, 135, 22.5]

# código clave-valor (dictionary) para descifrar
base = 16
hexadecimal_symbols = ['0', '1', '2', '3',
                       '4', '5', '6','7',
                       '8', '9', 'A', 'B',
                       'C', 'D','E', 'F']
degree = []
for i in range(0, base):
    degree.append(360/base*i)

code = {}
for key, value in zip(hexadecimal_symbols, degree):
    code[key] = value


# descifrar
def decode(message):
    # descifrar: degrees ---> hexadecimal symbols
    hexadecimal_message = ''
    for j in message:
        # recorre totalidad código anterior (code) y sólo devuelve cuando existe coincidencia
        for key, value in code.items():
            if value == j:
                hexadecimal_message += key
    # descifrar: hexadecimal symbols ---> ascii (ord) code ---> character
    decoded_menssage = ''
    # código hexadecimal = 2 símbolos
    for z in range(0, len(hexadecimal_message), 2):
        ascii_code  = int(hexadecimal_message[z:z+2] , base)
        character   = chr(ascii_code)
        decoded_menssage += character
    return decoded_menssage

decoded_menssage = decode(degree_message)
print('Mensaje Descifrado:', decoded_menssage)


# range(0, len = 8, step = 2)
# z = 0 ---> hexadecimal_message[0:2] = valores posiciones 0 y 1
# z = 2 ---> hexadecimal_message[2:4] = valores posiciones 2 y 3
# z = 4 ---> hexadecimal_message[4:6] = valores posiciones 4 y 5
# z = 6 ---> hexadecimal_message[6:8] = valores posiciones 6 y 7




