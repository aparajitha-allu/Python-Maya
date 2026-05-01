# Read input
n = int(input().strip())

a, b = 0, 1
even_sum = 0

while a <= n:
    if a % 2 == 0:
        even_sum += a
    a, b = b, a + b

print(even_sum)