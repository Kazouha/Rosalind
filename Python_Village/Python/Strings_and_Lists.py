# Given: A string s of length at most 200 letters and four integers a, b, c and d.
# Return: The slice of this string from indices a through b and c through d (with space in between),
# inclusively. In other words, we should include elements s[b] and s[d] in our slice.

# Reads file content into list
def read_file(file_name):
    return open(file_name, "r").readlines()

# Slices input string and returns list of slices
def string_slice(input, a, b, c, d):
    result = [input[a:b+1], input[c:d+1]]
    return result 


input = read_file("rosalind_ini3.txt")

slice_indices = [int(index) for index in input[1].split()]

result = string_slice(input[0], slice_indices[0], slice_indices[1], slice_indices[2], 
                      slice_indices[3])

print(result[0] + " " + result[1])
