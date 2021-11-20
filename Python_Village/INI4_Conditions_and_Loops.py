# Input variables
a = 100
b = 200

# Calculation
sum = 0

for i in range(a, b):
    if i % 2 == 1: # only adds i to sum if i is odd
        sum += i

print(sum)
