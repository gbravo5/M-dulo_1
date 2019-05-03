from ticket import set_tickets

# counter by type_admission
accum_type_quantity = {'Age 2 and under...............:': 0.0, 
                       'Age 2+ and 12.................:': 0.0, 
                       'General Admission.............:': 0.0, 
                       'Senior Admission (Age 65+)....:': 0.0}
                       
accum_type_cost     = {'Age 2 and under...............:': 0.0, 
                       'Age 2+ and 12.................:': 0.0, 
                       'General Admission.............:': 0.0, 
                       'Senior Admission (Age 65+)....:': 0.0}
                       
# counter total_units and total_invoice
accum_total = {'total_units'  : 0, 
               'total_invoice': 0}


def quantity_processing(record):
	accum_type_quantity[record[0]] += float(record[2].strip())
	return accum_type_quantity

def price(record):
	age      = float(record[1].strip())
	ticket   = set_tickets(age)
	price    = ticket[3]
	return price

def cost_processing(record, quantity):
	ticket_price = price(record)
	accum_type_cost[record[0]] = quantity[record[0]] * ticket_price
	return accum_type_cost

def total_processing(record):
	ticket_price = price(record)
	accum_total['total_units']   += float(record[2].strip())
	accum_total['total_invoice'] += float(record[2].strip()) * ticket_price
	return [accum_total['total_units'], accum_total['total_invoice']]
	
	

	
	


