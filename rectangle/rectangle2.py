import screen2

screen2.clear()

def rectangle(row, col, length, width, caracter):	
	for a in range(length - 1):
		screen2.locate(row, col + a, caracter)
		for b in range(width - 1):
			screen2.locate(row + b, col, caracter)
			for c in range(length):
				screen2.locate(row + (width - 1) , col + c, caracter)
				for d in range(width - 1):
					screen2.locate(row + d, col + length - 1, caracter)
					
rectangle(2, 50, 5, 3, '*')