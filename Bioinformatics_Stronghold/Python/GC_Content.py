# The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or
# 'G'. For example, the GC-content of "AGCTATAG" is 37.5%. Note that the reverse complement of any 
# DNA string has the same GC-content.
# DNA strings must be labeled when they are consolidated into a database. A commonly used method of 
# string labeling is called FASTA format. In this format, the string is introduced by a line that 
# begins with '>', followed by some labeling information. Subsequent lines contain the string 
# itself; the first line to begin with '>' indicates the label of the next string.
# In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx", 
# where "xxxx" denotes a four-digit code between 0000 and 9999.
#
# Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
# Return: The ID of the string having the highest GC-content, followed by the GC-content of that 
# string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise 
# stated; please see the note on absolute error below.

class FastaSequence:
    def __init__(self):
        self.id = None
        self.sequence = ""
        self.gc_content = None

    def set_id(self, id):
        self.id = id

    def set_sequence(self, DNA_string):
        if self.sequence == "":
            self.sequence = DNA_string
        else:
            self.sequence += DNA_string

    def set_gc_content(self, gc_content):
        self.gc_content = gc_content


# Creates FastaSequence objects from text file and reads them into list
def read_fasta(file_name):
    file_content = open(file_name, 'r').readlines()

    sequences = []
    sequence = None

    for line in file_content:
        if line.startswith('>'):
            sequence = FastaSequence()
            sequences.append(sequence)
            sequence.set_id(line.strip('>').strip('\n'))
        else:
            sequence.set_sequence(line.strip('\n'))
    
    return sequences

# Calculates GC content for list of FastaSequence objects
def calculate_gc_content(fasta_sequences):
    for sequence in fasta_sequences:
        count = 0

        for nt in sequence.sequence:
            if nt == 'G' or nt == 'C':
                count += 1
        
        sequence.set_gc_content((count / len(sequence.sequence)) * 100)
    


fasta_input = read_fasta("rosalind_gc.txt")

calculate_gc_content(fasta_input)

sorted_fasta = sorted(fasta_input, key=lambda x: x.gc_content, reverse=True)

print(sorted_fasta[0].id)
print(round(sorted_fasta[0].gc_content, 6))
