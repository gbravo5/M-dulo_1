from import_processing import quantity_processing, cost_processing, total_processing

dataset = open('transacciones.txt', 'r')
row     = dataset.readline()

while row != '':
	record   = row.split(',')
	quantity = quantity_processing(record)
	cost     = cost_processing(record, quantity)
	total    = total_processing(record) 
	row      = dataset.readline()


data_merge = {}
for i in quantity.keys():
	data_merge[i] = quantity[i], cost[i]
for key, value in data_merge.items():
	print('{}{:5.2f}{:7.2f}€'.format(key, value[0], value[1]))

total_units   = total[0]
total_invoice = total[1]
print('\nTotal.........................:{:5.2f} {:7.2f}€'.format(total_units, total_invoice))
	
	
	
	
	
	
	
	
	
	
	
	
	
# {key:(dict_one[key], dict_two[key]) for key in dict_one}	
