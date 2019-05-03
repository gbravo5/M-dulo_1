def celsiusTofahrenheit(x):
    return x * 9/5 + 32

def fahrenheitTocelsius(x):
    return(x - 32) * 5/9

def fahrenheit(start, end, step):
    for celsius in range(start, end + step, step):
        print ('{}º Celsius --> {}º Fahrenheit'.format(celsius, celsiusTofahrenheit(celsius)))

def celsius(start, end, step):
    for fahrenheit in range(start, end + step, step):
        print ('{}º Fahrenheit --> {}º Celsius'.format(fahrenheit, fahrenheitTocelsius(fahrenheit)))


type_degree = input('Si conversor de Celsius a Fahrenheit -> input C\nSi conversor de Fahrenheit a Celsius ---> input F\n')

if type_degree.lower() == 'c':
    fahrenheit(0, 230, 10)    
elif type_degree.lower() == 'f':
    celsius(0, 100, 100)
else:
    print('Error')




    

#def converter(type_degree, start, end, step):
    #if type_degree.lower() == 'c':
    #    fahrenheit(0, 230, 10)