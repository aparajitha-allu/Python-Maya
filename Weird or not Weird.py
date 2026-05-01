n = int(input().strip())

if n % 2 != 0:
    # Rule: If n is odd
    print("weird")
else:
    # n is even, now check the ranges
    if 2 <= n <= 5:
        print("not weird")
    elif 6 <= n <= 20:
        print("weird")
    else:
        # n is even and greater than 20
        print("not weird")