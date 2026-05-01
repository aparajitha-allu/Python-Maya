n = int(input())

a, b = 0, 1

while a < n:
    a, b = b, a + b

if n == a or n == 0:
    print("True")
else:
    print("False")