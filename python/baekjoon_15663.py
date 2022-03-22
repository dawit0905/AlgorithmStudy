import sys


def dfs(temp):
    if len(temp) == m:
        for i in temp:
            print(i, end=" ")
        print()
        return

    remember = 0
    for i in range(n):
        if visited[i] == 0 and remember != arr[i]:
            visited[i] = 1
            temp.append(arr[i])
            remember = arr[i]
            dfs(temp)
            visited[i] = 0
            temp.pop()


n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
visited = [0] * n

arr.sort()
temp = []
dfs(temp)