import sys

# Input
data = list(map(int, sys.stdin.read().split()))
X, Y, Z = data[0], data[1], data[2]

# Calculate maximum mangoes
max_mangoes = (Z - Y) // X

# Output
print(max_mangoes)  