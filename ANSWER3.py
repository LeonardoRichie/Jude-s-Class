"""
In 2001, the National Weather Service implemented a new wind-chill temperature formula to
measure the coldness using temperature and wind speed. The formula is:
where:
twc is the wind chill temperature
ta is the outside temperature
v is the wind speed
The formula can only be used for temperatures between -58 degrees Fahrenheit and 41
degrees Fahrenheit, as well as wind speeds greater than or equal to 2mph.
Write a program that:
• asks the user to enter a temperature between -58 degrees Fahrenheit and 41 degrees
Fahrenheit.
o Input validation: If the user enters a temperature not in range, use an if
statement or while loop to ask them to re-enter the value.
• asks the user to enter a windchill greater than 2mph.
o Input validation: If the user enters a wind speed not in range, use an if statement
or while loop to ask them to re-enter the value.
The program then calculates the wind-chill temperature using the formula above. Format the
output to 3 decimal places.
"""
y = int
b = int
x = int(input("Enter the temperature in Fahrenheit: "))
if -58 < x < 41:
    x = False
else:
    x = True
    print("Temperature must be between -58F and 41F")
while x:
    y = int(input("Please re-enter the temperature in Fahrenheit: "))
    if y < -58 or 41 < y:
        print("Temperature must be between -58F and 41F")
    if-58 < y < 41:
        x = False
a = int(input("Enter the wind speed miles per hour: "))
if 2 <= x:
    a = False
else:
    a = True
    print("Speed must be greater than or equal to 2")
while a:
    b = int(input("Please re-enter the wind speed miles per hour: "))
    if b < 2:
        print("Speed must be greater than or equal to 2")
    if 2 <= b:
        a = False
c = 35.74 + 0.6215*y - 35.75*(b**0.16) + 0.4275*y*(b**0.16)
d = ("{:.3f}".format(c))
print("The wind chill index is {0}".format(d))
