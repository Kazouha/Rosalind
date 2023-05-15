# An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.
# Given a DNA string t corresponding to a coding strand, its transcribed RNA string u is formed by
# replacing all occurrences of 'T' in t with 'U' in u.

# Given: A DNA string t having length at most 1000 nt.
# Return: The transcribed RNA string of t.

# Reads file content into list
def read_file(file_name):
    return open(file_name, "r").readline().strip()

# Converts DNA string to RNA
def dna_to_rna_converter(dna_string):
    rna_string = ""

    for nt in dna_string:
        if nt == 'T':
            rna_string += 'U'
        else:
            rna_string += nt

    return rna_string


input = read_file("rosalind_rna.txt")

print(dna_to_rna_converter(input))
