import sys


n, l = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

arr.sort()

cnt = 0
ran = 0
for i in arr:

    if i <= ran:
        continue

    ran = i - 0.5 + l
    cnt += 1

print(cnt)