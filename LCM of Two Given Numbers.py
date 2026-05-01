import math

# Input: Read M and N
m, n = map(int, input().split())

# Use the math library to find LCM directly
result = math.lcm(m, n)

# Output
print(result)