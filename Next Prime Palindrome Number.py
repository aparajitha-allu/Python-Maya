# Function to check palindrome
def is_palindrome(n):
    return str(n) == str(n)[::-1]

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

num = n + 1

# Find next prime palindrome
while True:
    if is_palindrome(num) and is_prime(num):
        print(num)
        break
    num += 1