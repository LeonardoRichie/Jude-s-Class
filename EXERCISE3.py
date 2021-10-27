"""
Write a function called num atoms() that calculates how many atoms are in n grams of an element given its atomic weight.
 This function should take two parameters: the amount of the element in grams and an optional argument representing the
 atomic weight of the element. The atomic weight of any particular element can be found on a periodic table but make the
 default value for the optional argument the atomic weight of gold (Au) 196.97 with units in grams/mole. A mole is a
 unit of measurement that is commonly used in chemistry to express an amount of a substance. Avogadro’s number is a
 constant, 6:022_1023 atoms/mole, that can be used to find the number of atoms in a given sample. Use Avogadro’s number,
 the atomic weight, and the amount of the element in grams to find the number of atoms present in the sample. Your
 function should return this value.
"""


def num_atoms(x, y=196.97):
    result = ((x / y) * (6.022 * 10**23))
    print(result)


print("num_atoms(10)")
num_atoms(10)
print("num_atoms(10, 12.001)")
num_atoms(10, 12.001)
print("num_atoms(10, 1.008)")
num_atoms(10, 1.008)
