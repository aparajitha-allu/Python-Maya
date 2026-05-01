import sys

data = list(map(int, sys.stdin.read().split()))
x, y = data[0], data[1]

print(2*x - y)