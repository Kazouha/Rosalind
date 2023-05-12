# Given: A string s of length at most 10000 letters.
# Return: The number of occurrences of each word in s, where words are separated by spaces. Words
# are case-sensitive, and the lines in the output can be in any order.

# Reads file content into string
def read_file(file_name):
    input = open(file_name, "r").readlines()
    return input[0]

# Counts number of occurences (case-sensitive) of words into a dict
def number_of_occurences(input):
    single_words = input.split()
    word_dict = dict()

    for word in single_words:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    
    return word_dict

input = read_file("rosalind_ini6.txt")

word_dict = number_of_occurences(input)

for word in word_dict:
    print(word + " " + str(word_dict.get(word)))