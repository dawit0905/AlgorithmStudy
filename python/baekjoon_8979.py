import sys


n, m = map(int, sys.stdin.readline().split())
arr = []
memo = [0] * (n+1)
for i in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    arr.append(tmp)
arr.sort(key=lambda x: (-x[1], -x[2], -x[3]))

index = 0
for i in range(n):
    if arr[i][0] == m:
        index = i
        break

for i in range(n):
    if arr[index][1:] == arr[i][1:]:
        print(i+1)
        break
