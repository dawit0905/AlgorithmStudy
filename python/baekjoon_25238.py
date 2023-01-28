import sys


a, b = map(int, sys.stdin.readline().split())

result = int(a - (a * (b * 0.01)))
print(1) if result < 100 else print(0)
