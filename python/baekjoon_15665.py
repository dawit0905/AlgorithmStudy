import sys


def dfs(temp):
    if len(temp) == m:
        for i in temp:
            print(i, end=" ")
        print()
        return
    remember = 0
    for i in range(n):
        if remember != arr[i]:
            remember = arr[i]
            temp.append(arr[i])
            dfs(temp)
            temp.pop()


n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
temp = []
visited = [0] * n

dfs(temp)
