import sys

sum = 0
total = 0
for i in range(4):
    a, b = map(int, sys.stdin.readline().split())
    sum += b - a
    total = max(total, sum)

print(total)