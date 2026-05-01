n = int(input())

def is_palindrome(x):
    return str(x) == str(x)[::-1]

d = 1

while True:
    lower = n - d
    upper = n + d

    found_lower = lower >= 0 and is_palindrome(lower)
    found_upper = is_palindrome(upper)

    if found_lower and found_upper:
        print(lower, upper)   # FIX: smaller first
        break
    elif found_lower:
        print(lower)
        break
    elif found_upper:
        print(upper)
        break

    d += 1