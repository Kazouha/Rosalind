# A sequence is an ordered collection of objects (usually numbers), which are allowed to repeat. 
# Sequences can be finite or infinite. Two examples are the finite sequence (π,–√(2),0,π) and the 
# infinite sequence of odd numbers (1,3,5,7,9,…). We use the notation an to represent the n-th term 
# of a sequence.
# A recurrence relation is a way of defining the terms of a sequence with respect to the values of 
# previous terms. In the case of Fibonacci's rabbits from the introduction, any given month will 
# contain the rabbits that were alive the previous month, plus any new offspring. A key observation 
# is that the number of offspring in any month is equal to the number of rabbits that were alive two
# months prior. As a result, if F_n represents the number of rabbit pairs alive after the n-th 
# month,then we obtain the Fibonacci sequence having terms F_n that are defined by the recurrence 
# relation F_n=F_n−1+F_n−2 (with F_1=F_2=1 to initiate the sequence). Although the sequence bears 
# Fibonacci's name, it was known to Indian mathematicians over two millennia ago.
# When finding the n-th term of a sequence defined by a recurrence relation, we can simply use the 
# recurrence relation to generate terms for progressively larger values of n. This problem 
# introduces us to the computational technique of dynamic programming, which successively builds up 
# solutions by using the answers to smaller cases.
#
# Given: Positive integers n ≤ 40 and k ≤ 5.
# Return: The total number of rabbit pairs that will be present after n months, if we begin with 1 
# pair and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit 
# pairs (instead of only 1 pair).

# Reads file content into list
def read_file(file_name):
    return open(file_name, "r").readline().split()

def fibonacci_rabbits(n, k):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci_rabbits(n-1, k) + k * fibonacci_rabbits(n-2, k)
    


values = [int(value) for value in read_file("rosalind_fib.txt")]

print(fibonacci_rabbits(values[0], values[1]))