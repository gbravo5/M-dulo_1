import screen

def label():
	screen.clear()
	
	screen.Print('Age 2 and under...............:     -', row = 4, col = 5)
	screen.Print('Age 2+ and 12.................:     -', row = 5, col = 5)
	screen.Print('General Admission.............:     -', row = 6, col = 5)
	screen.Print('Senior Admission (Age 65+)....:     -', row = 7, col = 5)
	
	screen.Print('Total.........................:     -', row = 9, col = 5, style = 'bold')

	
