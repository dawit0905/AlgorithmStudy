import sys

n, m = map(int, sys.stdin.readline().split())
number = sys.maxsize
total = 0
arr = [[0]*2 for _ in range(m)]
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    arr[i][0] = a
    arr[i][1] = b

while n != 0:
    number = sys.maxsize

    for i in range(m):
        number = min(arr[i][0], number)
        number = min(arr[i][1] * n, number)
    if n < 6:
        n = n-n
    else:
        n = n-6
    total += number

print(total)