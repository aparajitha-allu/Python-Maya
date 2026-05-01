n = int(input())

digits = str(n)
total = 0

for i in range(len(digits)):
    total += int(digits[i]) ** (i + 1)

if total == n:
    print("True")
else:
    print("False")