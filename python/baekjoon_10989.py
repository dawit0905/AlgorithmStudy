import sys

n = int(sys.stdin.readline().rstrip())

data = [0] * 10001

for i in range(n):
    a = int(sys.stdin.readline().rstrip())
    data[a] += 1

for i in range(10001):
    if data[i] != 0:
        for _ in range(data[i]):
            print(i)