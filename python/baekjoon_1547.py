import sys


m = int(sys.stdin.readline())
ball = 1

for i in range(m):
    x, y = map(int, sys.stdin.readline().split())
    if x == ball:
        ball = y
    elif y == ball:
        ball = x

print(ball)