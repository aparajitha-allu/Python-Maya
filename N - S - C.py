# Read input
A, B = map(int, input().split())

# Loop from A+1 to B-1
for n in range(A + 1, B):
    print(n, n**2, n**3)