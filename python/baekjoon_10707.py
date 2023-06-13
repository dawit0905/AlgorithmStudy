import sys


A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())
D = int(sys.stdin.readline())
P = int(sys.stdin.readline())

x = A * P

if P <= C:
    y = B
else:
    y = B + (P - C) * D

print(min(x, y))