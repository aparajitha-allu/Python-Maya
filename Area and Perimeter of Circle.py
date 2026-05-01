import sys

# Input
r = int(sys.stdin.read().strip())

pi = 3.14

# Calculations
area = pi * r * r
perimeter = 2 * pi * r

# Output (2 decimal places)
print(f"{area:.2f}")
print(f"{perimeter:.2f}")