p = int(input())
r = int(input())
t = int(input())

ci = p * ((1 + r/100) ** t - 1)

print("{:.2f}".format(ci))