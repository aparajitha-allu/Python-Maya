n = int(input())

# Ugly numbers are positive only
if n <= 0:
    print("Not Ugly Number")
else:
    for i in [2, 3, 5]:
        while n % i == 0:
            n //= i

    if n == 1:
        print("Ugly Number")
    else:
        print("Not Ugly Number")   