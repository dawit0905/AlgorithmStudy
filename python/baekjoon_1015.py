import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
p = [0] * n

for i in range(n):
    temp = arr.index(min(arr))
    p[temp] = i
    arr[temp] = 1001

print(*p)

