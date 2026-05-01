# Read input
n = int(input().strip())

fact = 1

# Calculate factorial
for i in range(1, n + 1):
    fact *= i

# Print result
print(fact)
