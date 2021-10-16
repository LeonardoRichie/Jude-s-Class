"""
A software company sells a package that retails for $99. Discounts for quantities are given
according to the following table:
Quantity Discount
10 -19 10%
20 - 49 20%
50 - 99 30%
100 or more 40%
Write a program that asks the user to enter the number of packages purchased. The program
should then display the amount of the discount (if any) and the total of the purchase after the
discount. (Use appropriate formatting to display currency and percentages in your output.)
"""

y = int
x = int(input("Enter the number of packages purchased: "))
if x < 10:
    y = 0
if 10 <= x <= 19:
    y = 10
if 20 <= x <= 49:
    y = 20
if 50 <= x <= 99:
    y = 30
if 100 <= x:
    y = 40
b = 99*x/100*y
z = ("{:,.2f}".format(99*x/100*y))
"""
y = Discount
z = Discount Amount"""

a = (x*99)-b
amount1 = ("{:.2f}".format(a))
print("Discount Amount @ {0}%: $ {1}".format(y, z))
print("Total Amount: $ {0}".format(amount1))
