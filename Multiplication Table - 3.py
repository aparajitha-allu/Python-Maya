# Read input
N, A, B = map(int, input().split())

# Print multiplication table
for i in range(A, B + 1):
    print(f"{N} x {i} = {N * i}")