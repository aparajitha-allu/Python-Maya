# Function to check prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Read input
n = int(input().strip())

# If already prime
if is_prime(n):
    print(0)
else:
    # Find next prime > n
    up = n + 1
    while not is_prime(up):
        up += 1

    # Find previous prime < n
    down = n - 1
    while down >= 2 and not is_prime(down):
        down -= 1

    # Calculate differences
    diff_up = up - n
    diff_down = n - down if down >= 2 else float('inf')

    print(min(diff_up, diff_down))