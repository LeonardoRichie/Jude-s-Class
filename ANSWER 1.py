"""
Write a program that prompts the user to enter the coordinates of two points (x1, y1) and (x2,
y2). The program should calculate and display the slope of the line that connects the two points.
The formula for the slope is !!"!"
#!"#"
.
Format your output to five decimal places.
"""

a = float(input("Enter the x-coordinate for point1:"))
b = float(input("Enter the y-coordinate for point1:"))
c = float(input("Enter the x-coordinate for point2:"))
d = float(input("Enter the y-coordinate for point2:"))

x = (d-b)/(c-a)
y = round(x, 5)
print("The slope for the line that connects two points ({0},{1}) and ({2},{3}) is {4}".format(a, b, c, d, y))
