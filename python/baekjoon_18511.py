import sys


def recursion(cnt, temp):
    global result, n
    if cnt > len(str(n)):
        return
    if cnt >= 1 and n >= int(''.join(temp)) and result < int(''.join(temp)):
        result = int(''.join(temp))

    for i in arr:
        temp.append(i)
        recursion(cnt+1, temp)
        temp.pop()


n, k = map(int, sys.stdin.readline().split())
arr = list(map(str, sys.stdin.readline().split()))

temp = []
result = 0
recursion(0, temp)

print(result)