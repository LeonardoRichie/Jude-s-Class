"""
Given this information, write a program that prompts the user to enter the Force and mass of
the cart. (Store the value of g as a ‘constant’ in your program) The program should then use the
formula to calculate the angle of the ramp. Format your output to 1 decimal place.
Note: The trigonometric functions in the math module returns the values in radians. In addition
to the arc sin function (asin), you will need to use the degrees function to convert the angle to
degrees.
"""

import math
m = int(input("Enter the mass of the cart (in kg):"))
f = int(input("Enter the force to push the cart (in N):"))
x = f / 9.8 / m
y = math.asin(x)
z = y * 57.2958
e = round(z, 1)
print("The angle of the ramp is {0} degrees".format(e))
