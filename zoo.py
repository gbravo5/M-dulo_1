import screen
from display import label
from validation import valid
from ticket import process_tickets, collect_data, save_data


def main():

	label()

	age      = valid('Introduzca Edad: ')
	quantity = valid('Introduzca Cantidad: ')
	
	data = []
	
	while age > 0 and quantity > 0:
	
		tickets = process_tickets(age, quantity)
		
		collect_data(data, tickets)
		
		screen.Print(tickets[1], row = tickets[3][0], col = tickets[3][1])
		screen.Print('{:7.2f}€'.format(tickets[2]), row = tickets[4][0], col = tickets[4][1])
		
		screen.Print(tickets[5], row = tickets[7][0], col = tickets[7][1], style = 'bold')
		screen.Print('{:7.2f}€'.format(tickets[6]), row = tickets[8][0], col = tickets[8][1], style = 'bold')
		
		age = valid('Introduzca Edad: ')
		if age == 0:
			continue
		else:
			quantity = valid('Introduzca Cantidad: ')
	
	save_data(data)

	screen.locate(15, 1)
	
main()