import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

# print(arr.count(n))

cnt = 0
for i in arr:
    if i == n:
        cnt += 1

print(cnt)