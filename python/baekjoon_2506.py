import sys


n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

_sum = 0
cnt = 0
for i in arr:

    if i == 1:
        cnt += 1
    else:
        cnt = 0

    _sum += cnt

print(_sum)