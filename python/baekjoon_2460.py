import sys


result = 0
now = 0
for i in range(10):
    a, b = map(int, sys.stdin.readline().split())
    now -= a
    result = max(result, now)
    now += b
    result = max(result, now)

print(result)
