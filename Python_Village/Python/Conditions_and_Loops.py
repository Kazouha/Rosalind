# Given: Two positive integers a and b (a < b < 10000).
# Return: The sum of all odd integers from a through b, inclusively.

# Reads file content into list
def read_file(file_name):
    return open(file_name, "r").readline().split()

# Takes two integers and returns sum of odd integers in range
def sum_of_odds(a, b):
    sum = 0

    for i in range(a, b+1):
        if i % 2 == 1:
            sum += i

    return sum


values = [int(value) for value in read_file("rosalind_ini4.txt")]

print(sum_of_odds(values[0], values[1]))
