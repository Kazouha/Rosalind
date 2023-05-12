# Given: A file containing at most 1000 lines.
# Return: A file containing all the even-numbered lines from the original file. Assume 1-based
# numbering of lines.

# Reads file content into list
def read_file(file_name):
    return open(file_name, "r").readlines()

def even_lines_to_file(input, file_name):
    file = open(file_name, "w")

    counter = 1

    for line in input:
        if counter % 2 == 0:
            file.write(line)
        
        counter += 1
    

input = read_file("rosalind_ini5.txt")

even_lines_to_file(input, "rosalind_ini5_solution.txt")