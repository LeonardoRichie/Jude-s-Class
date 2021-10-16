"""
Write a program that reads the subtotal and gratuity rate. The program then calculates and
gratuity as a dollar amount, followed by the total amount, and displays all information in
dollars.
Your code should include currency formatting (i.e., use the $ in your output, include comma
separation and format the result to 2 decimal places.)
"""

v = (input("Enter the subtotal:"))
y = float(input("Enter tip amount (as a%):"))
x = int(v.strip('$'))
z = x/100*25
a = x + z
"""Adding decimal"""
"""b = (format(x, ".2f"))
c = (format(z, ".2f"))
d = (format(a, ".2f"))"""
"""Adding commas"""
b = "{:,.2f}".format(x)
c = "{:,.2f}".format(z)
d = "{:,.2f}".format(a)

print("subtotal: $ {0}". format(b))
print("Tip: $ {0}". format(c))
print("Total: $ {0}".format(d))
