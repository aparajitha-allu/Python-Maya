# Input
a = int(input())
b = int(input())

# Swapping without temp variable
a = a + b
b = a - b
a = a - b

# Output
print(a)
print(b)