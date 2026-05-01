# Function to check prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Read input
n1 = int(input().strip())
n2 = int(input().strip())

S = n1 + n2

x = 1

# Find minimum x
while True:
    if is_prime(S + x):
        print(x)
        break
    x += 1