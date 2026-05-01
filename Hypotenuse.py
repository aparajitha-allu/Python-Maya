import math

# Input
x, y = map(int, input().split())

# Calculate hypotenuse
hypotenuse = math.sqrt(x*x + y*y)

# Output (2 decimal places)
print(f"{hypotenuse:.2f}")