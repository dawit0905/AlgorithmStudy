import sys


def dfs(temp, num):
    if len(temp) == m:
        for i in temp:
            print(i, end=" ")
        print()
        return
    for i in range(n):
        if arr[i] >= num:
            temp.append(arr[i])
            dfs(temp, arr[i])
            temp.pop()


n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
temp = []
dfs(temp, arr[0])