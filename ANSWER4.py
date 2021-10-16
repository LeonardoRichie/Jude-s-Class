"""
Write a program that prompts the user to enter the side of a hexagon and displays its area. The
area of a hexagon is '√'
% 𝑠%. Assume that the side entered is positive.
Format the result to three decimal places. Use the functions pow and sqrt from the math
module to express the formula accurately. (See section 2.9 in your zyBook to review the math
module.)
"""

import math
x = float(input("Enter the side length of the hexagon: "))
y = (math.sqrt(3))*3/2*x**2
z = (format(y, ".3f"))
print("The area of a hexagon with side length 5.5 is {0}".format(z))
