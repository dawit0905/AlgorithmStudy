import sys


a, b = map(int, sys.stdin.readline().split())
if a > b:
    a, b = b, a

n = b - a- 1
if a == b or a+1 == b:
    n = 0

print(n)
for i in range(a+1, b):
    print(i, end=" ")
