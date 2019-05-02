from es_decimal_positivo import esDecimalPositivo
import screen

def valid(message):
	nb_str = screen.Input(message, row = 1, col = 1)
	while not esDecimalPositivo(nb_str):
		screen.Print('Input Inválido: ' + nb_str + ' debe ser un número positivo', 
		             row = 25, col = 1,
		             style = 'bold', color = 'yellow', fill = 'red')
		nb_str = screen.Input(message, row = 1, col = 1)
	screen.Print('\033[K', row = 25, col = 1)
	return float(nb_str)