import sys


n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

cnt = 0
answer = 0
for i in range(n):
    if arr[i] >= 1:
        cnt += 1
    else:
        cnt = 0

    answer = max(answer, cnt)

print(answer)