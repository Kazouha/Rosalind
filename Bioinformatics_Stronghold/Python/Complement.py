# In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.
# The reverse complement of a DNA string s is the string s^c formed by reversing the symbols of s, 
# then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").
#
# Given: A DNA string s of length at most 1000 bp.
# Return: The reverse complement sc of s.

# Reads file content into list
def read_file(file_name):
    return open(file_name, "r").readline().strip()

# Gives the reverse complement of a DNA string
def reverse_complement(DNA_string):
    nt_complements = {'A': 'T', 'G': 'C', 'T': 'A', 'C': 'G'}

    complement = ""

    for nt in DNA_string:
        complement += nt_complements[nt]

    return complement[::-1]


input = read_file("rosalind_revc.txt")

print(reverse_complement(input))
