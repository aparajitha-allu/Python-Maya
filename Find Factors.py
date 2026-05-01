# Read input
n = int(input())

# Find and print factors
for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")