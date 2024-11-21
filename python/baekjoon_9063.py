import sys


n = int(sys.stdin.readline())


x_max = -10001
x_min = 10001
y_max = -10001
y_min = 10001
for i in range(n):
    a, b = (map(int, sys.stdin.readline().split()))
    x_max = max(x_max, a)
    x_min = min(x_min, a)
    y_max = max(y_max, b)
    y_min = min(y_min, b)

if n == 1:
    print(0)
else:
    print((x_max-x_min) * (y_max - y_min))

