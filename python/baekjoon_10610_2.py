import sys


arr = list(sys.stdin.readline().strip())
arr.sort(reverse=True)
flag = 0
for i in range(len(arr)):
    n = ''
    for j in arr:
        n += j
    if int(n) % 30 == 0:
        flag = 1
    if flag:
        print(n)
        exit(0)
    arr.append(arr.pop(0))

print(-1)