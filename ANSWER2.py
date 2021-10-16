"""
Write a program that reads the three edges of a triangle and computes the perimeter if the
input is valid. The input is valid if the sum of every pair of two edges is greater than the
remaining edge. Otherwise (i.e. else) print a message stating that the input is invalid and the
perimeter cannot be calculated. (Note: This question does NOT require further input
validation.)
"""
x = float(input("Enter length of edge1: "))
y = float(input("Enter length of edge2: "))
z = float(input("Enter length of edge3: "))

if x + y > z and y + z > x and x + z > y:
    print("The perimeter is {0}".format(x+y+z))
else:
    print("Perimeter cannot be calculated: the input is invalid.")
