import sys


n = int(sys.stdin.readline())
arr = [[0] * 101 for _ in range(101)]

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    for i in range(y, y+10):
        for j in range(x, x+10):
            arr[i][j] = 1


cnt = 0
for i in range(1, 101):
    for j in range(1, 101):
        if arr[i][j] == 1:
            cnt += 1

print(cnt)
