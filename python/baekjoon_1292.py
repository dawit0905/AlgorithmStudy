import sys

a, b = map(int, sys.stdin.readline().split())

arr = [0] * 1001
num = 1
cnt = 0
i = 1
while i <= 1000:
    arr[i] = num
    cnt += 1

    if num == cnt:
        num += 1
        cnt = 0
    i += 1

print(sum(arr[a:b+1]))
