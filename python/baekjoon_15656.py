import sys


def dfs(temp):
    if len(temp) == m:
        for i in temp:
            print(i, end=" ")
        print()
        return
    for i in range(n):
        temp.append(arr[i])
        dfs(temp)
        temp.pop()


n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
temp = []
dfs(temp)