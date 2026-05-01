# Read input
n = int(input().strip())

# Generate odd numbers
odds = [str(i) for i in range(1, n + 1, 2)]

# Print in required format
print(" ".join(odds))