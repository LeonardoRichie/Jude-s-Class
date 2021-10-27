"""
Write a function called convert temp() that takes no arguments. This function obtains a temperature in
Fahrenheit from the user and uses two helper functions to convert this temperature to Celsius and Kelvin.
Write a helper function called convert to celsius() that takes a single argument in Fahrenheit and returns
the temperature in Celsius using the formula
where Tc is the temperature in Celsius and Tf is the temperature in Fahrenheit. Write another helper
function called convert to kelvin() that takes a single argument in degrees Celsius and returns degrees
Kelvin using the formula
where Tk is the temperature in Kelvin. Use these two functions within your convert temp() function to
display (i.e., print) the temperatures for the user. The convert temp() does not return anything.
"""


def convert_temp():
    x = int(input("The temperature in fahrenheit is: "))
    print()
    convert_to_celsius(x)
    y = convert_to_celsius(x)
    z = convert_to_kelvin(y)
    print("The temperature in Fahrenheit is: {0}".format(x))
    print("The temperature in Celsius is: {0}".format(y))
    print("The temperature in Kelvin is: {0}".format(z))


def convert_to_celsius(x):
    result = (x-32)* 5 / 9
    return result


def convert_to_kelvin(y):
    result = y + 273.15
    return result


convert_temp()
