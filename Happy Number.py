n = int(input())

def sum_of_squares(num):
    total = 0
    while num > 0:
        digit = num % 10
        total += digit * digit
        num //= 10
    return total

visited = set()

while n not in visited:
    if n == 1 or n == 7:
        print("True")
        break
    
    visited.add(n)
    n = sum_of_squares(n)

else:
    print("False")