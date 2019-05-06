#erase display
def clear():
    print('\033[2J')


# cursor position
def locate(row, column, caracter, end = ''):
    print('\033[{};{}H{}{}'.format(row, column, caracter, end))