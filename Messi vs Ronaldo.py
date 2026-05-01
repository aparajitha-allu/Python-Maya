# Read input
A, B, X, Y = map(int, input().split())

# Calculate points
messi = 2 * A + B
ronaldo = 2 * X + Y

# Compare
if messi > ronaldo:
    print("Messi")
elif ronaldo > messi:
    print("Ronaldo")
else:
    print("Equal")