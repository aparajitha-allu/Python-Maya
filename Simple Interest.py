import sys

# Input
data = list(map(int, sys.stdin.read().split()))
P, T, R = data[0], data[1], data[2]

# Calculate Simple Interest
SI = (P * T * R) // 100

# Output
print(SI)