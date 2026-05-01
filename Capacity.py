import sys
data = list(map(int, sys.stdin.read().split()))
T, S, B = data[0], data[1], data[2]

bytes_total = 2 * T * S * B * 512
print(f"{bytes_total // 1024} KB")