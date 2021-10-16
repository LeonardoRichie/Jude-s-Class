"""
Given an airplane’s acceleration, a, and take-off speed, v, the minimum runway length needed
for the airplane to take off is computed using the formula $!
%& .
Write a program that prompts the user to enter the speed in meters per second (m/s) and the
acceleration in meters per second squared (m/s2). The program should calculate and display the
minimum runway length. Format the result to four decimal places. (For this question, assume
that all values entered are positive.)
"""

x = float(input("Enter the plane's take off speed in m/s:"))
y = float(input("Enter the plane's acceleration in m/s**2:"))
z = ((x**2)/(2*y))
a = round(z, 4)
print("The minimum runway length needed for this airplane is {0} meters". format(a))
