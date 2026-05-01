# Read input
X, Y = map(int, input().split())

# Calculate donation
donation = abs(Y - X)

print(donation)