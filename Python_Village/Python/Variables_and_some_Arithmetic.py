# Given: Two positive integers a and b, each less than 1000.
#Return: The integer corresponding to the square of the hypotenuse of the right triangle whose legs
#have lengths a and b.

import sys

# Reads file content into list
def read_file(file_name):
    return open(file_name, "r").readline().split()

# Calculates squared hypotenuse of right triangle with legs a and b
def hyp_squared(a, b):
    return a**2 + b**2


values = read_file("rosalind_ini2.txt")
print(hyp_squared(int(values[0]), int(values[1])))
