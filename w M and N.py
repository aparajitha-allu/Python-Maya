# Read input
M, N = map(int, input().split())

count = 0

# Loop from M to N (inclusive)
for i in range(M, N + 1):
    if i % 6 == 0:
        count += 1

print(count)