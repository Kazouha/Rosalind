# A string is simply an ordered collection of symbols selected from some alphabet and formed into a 
# word; the length of a string is the number of symbols that it contains.
#
# An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') 
# is "ATGCTTCAGAAAGGTCTTACG."
# 
# Given: A DNA string s of length at most 1000 nt.
# Return: Four integers (separated by spaces) counting the respective number of times that the 
# symbols 'A', 'C', 'G', and 'T' occur in s.

# Reads file content into list
def read_file(file_name):
    return open(file_name, "r").readline().strip()

# Counts nucleotides in a DNA string
def nucleotide_counter(DNA_string):
    nt_counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

    for nt in str(DNA_string):
        nt_counts[nt] += 1

    return nt_counts


input = read_file("rosalind_dna.txt")

nt_counts = nucleotide_counter(input)

print(str(nt_counts['A']) + ' ' + str(nt_counts['C']) + ' ' + str(nt_counts['G']) + ' ' + 
      str(nt_counts['T']))
