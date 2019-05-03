# counter units by type_admission
accum_type = {'Age 2 and under...............:': 0, 
              'Age 2+ and 12.................:': 0, 
              'General Admission.............:': 0, 
              'Senior Admission (Age 65+)....:': 0}
         
# counter total_units and total_invoice
accum_total = {'total_units'  : 0, 
               'total_invoice': 0}
               
# set parameters
def set_tickets(age):
    # Type
    # Child Admission:
    	# a) (Age 2 and under)
	if age > 0 and age <= 2:
		type = 'Age 2 and under...............:'
		row = 4
		col = 5
		price = 0.0
		return [type, row, col, price]
		
    	# b) (Age 2+ and 12)
	elif age <= 12:
		type = 'Age 2+ and 12.................:'
		row = 5
		col = 5
		price = 14.0
		return [type, row, col, price]
		
    # Senior Admission (Age 65+):
	elif age >= 65:
		type = 'Senior Admission (Age 65+)....:'
		row = 7
		col = 5
		price = 18.0
		return [type, row, col, price]
	# General Admission:
	else:
		type = 'General Admission.............:'
		row = 6
		col = 5
		price = 23.0
		return [type, row, col, price]

# process tickets
def process_tickets(age, quantity):
	
	selection = set_tickets(age)
	
	# by type_admission	
	accum_type[selection[0]] += quantity
	total_cost = accum_type[selection[0]] * selection[3]
	location_quantity = (selection[1], selection[2] + len(selection[0]))
	location_total_cost = (location_quantity[0], location_quantity[1] + 7)
	
	# by total
	accum_total['total_units']   += quantity
	accum_total['total_invoice'] += quantity * selection[3]
	location_total_units = (9, len('Total.........................:') + 5)
	location_total_invoice = (9, len('Total.........................:') + 5 + 7)
	
	# by record
	nb   = quantity
	cost = quantity * selection[3]
		
	return [selection[0], 
	        accum_type[selection[0]], total_cost, 
	        location_quantity, location_total_cost, 
	        accum_total['total_units'], accum_total['total_invoice'], 
	        location_total_units, location_total_invoice, 
	        age, nb, selection[3], cost]

# data processing:
	# a) collect information
def collect_data(data, tickets):

	record = [tickets[0], tickets[9], tickets[10], tickets[11], tickets[12]]
	data.append(record)

	# b) save data
def save_data(data):

	dataset = open('transacciones.txt', 'a+')
	
	for i in range(len(data)):
		transaccion = '{}, {}, {}, {}, {}\n'.format(data[i][0], data[i][1], 
		                                        data[i][2], data[i][3], 
		                                        data[i][4])	                                                        
		dataset.write(transaccion)
	
	dataset.close()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	        
	        
