start = int(input())
end = int(input())

for num in range(start, end + 1):
    if str(num) == str(num)[::-1]:
        print(num, end=" ")