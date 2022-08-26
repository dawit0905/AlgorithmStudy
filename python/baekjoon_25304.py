import sys


answer = int(sys.stdin.readline())
cnt = int(sys.stdin.readline())
total = 0

for i in range(cnt):
    a, b = map(int, sys.stdin.readline().split())
    total += a*b

if answer == total:
    print('Yes')
else:
    print('No')

