"""Write a function called convert to days() that takes no parameters. Have your function prompt the user
to input numbers of hours, minutes, and seconds. Write a helper function called get days() that uses these
values and converts them to days in float form (fractions of a day are allowed). get days() should return the
number of days. Use this helper function within the convert to days() function to display the numbers of
days to the user. The built-in function round() takes two arguments: a number and an integer indicating
the desired precision (i.e., the desired number of digits beyond the decimal point). Use this function to
round the number of days four digits after the decimal point."""


def convert_to_days():
    x = int(input("input the number of hours: "))
    y = int(input("input the number of minutes: "))
    z = int(input("input the number of seconds: "))
    print()
    get_days(x, y, z)


def get_days(x, y, z):
    a = x * 3600 + y * 60 + z
    result = round(a / 86400, 4)
    print("The number of days is: {0}". format(result))
    """CONVERT HOURS,MINUTES AND SECONDS INTO DAYS
    AND ROUND THE DECIMALS"""

convert_to_days()
