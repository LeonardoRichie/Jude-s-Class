"""
def calc_weight_on_planet(x, y=23.1):
    if y == 9.8:
        result = round((x * y) / 9.8, 2)
        print(result)
    else:
        result = (x * y) / 9.8
        print(result)

print("calc_weight_on_planet(120, 9.8)")
calc_weight_on_planet(120, 9.8)
print("calc_weight_on_planet(120)")
calc_weight_on_planet(120)
print("calc_weight_on_planet(120, 23.1)")
calc_weight_on_planet(120, 23.1)
"""


def calc_weight_on_planet(x, y=23.1):
    if y == 9.8:
        result = round((x * y) / 9.8, 2)
        print(result)
        """Earth"""
    else:
        result = (x * y) / 9.8
        print(result)
        """OTHER PLANET"""


print("calc_weight_on_planet(120, 9.8)")
calc_weight_on_planet(120, 9.8)
print("calc_weight_on_planet(120)")
calc_weight_on_planet(120)
print("calc_weight_on_planet(120, 23.1)")
calc_weight_on_planet(120, 23.1)
