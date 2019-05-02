import click

# set graphics mode:
# a) FontStyle
fontstyle = {'bold': 1, 'underline': 4, 'blink': 5, 'reversed': 7}
# b) FontColor
fontcolor = {'black': '30', 'red': '31', 'green': '32', 'yellow': '33',
             'blue': '34', 'magenta': '35', 'cyan': '36', 'white': '37',
             'reset': '39'}
# c) FillColor
fillcolor = {'black': '40', 'red': '41', 'green': '42', 'yellow': '43',
             'blue': '44', 'magenta': '45', 'cyan': '46', 'white': '47',
             'reset': '49'}

# erase display
def clear():
	print('\033[2J')
    
# erase line (delete previous input)
def clearLine():                                                  
	print('\033[K', end = '')

# cursor position
def locate(row, col):
	print('\033[{};{}H'.format(row, col), end = '')

# process graphics mode:
def parameters(graphics_mode):
	if 'row' in graphics_mode:
		row = graphics_mode['row']
		col = 1 # default value
		if 'col' in graphics_mode:
			col = graphics_mode['col']					
		locate(row, col)
		
	if 'color' in graphics_mode and graphics_mode['color'] in fontcolor:
		print('\033[{}m'.format(fontcolor[graphics_mode['color']]), end = '')
	
	if 'fill' in graphics_mode and graphics_mode['fill'] in fillcolor:
		print('\033[{}m'.format(fillcolor[graphics_mode['fill']]), end = '')
	
	if 'style' in graphics_mode and graphics_mode['style'] in fontstyle:
		print('\033[{}m'.format(fontstyle[graphics_mode['style']]), end = '')

# reset
def Reset():
	print('\033[0m', end = '')

# print customized
def Print(str, **graphics_mode):
	parameters(graphics_mode)
	if 'new_line' in graphics_mode and graphics_mode['new_line']:
		# se genera salto de línea
		print(str)
	else:
		# no se genera salto de línea
		print(str, end = '')
	if 'new_reset' not in graphics_mode:
		Reset()
	
# input customized
def Input(message, **graphics_mode):
	parameters(graphics_mode)
	if 'dirty' not in graphics_mode:
		clearLine()
	return input(message)

# format customized
def Format (fontstyle, fontcolor = 'white', fillcolor = 'black'):
	click.style
	
	
# (1) graphics_mode: ( row = integer , col = integer , color = 'string' , fill = 'string' , style = 'string', 
#                      new_line = True/False , new_reset = True/False, dirty = True/False )
# (2)
#     color = 'string',  
#     fill  = 'string',  
#     style = 'string' 
#     string xq son las keys de fontstyle, fontcolor y fillcolor respectivamente