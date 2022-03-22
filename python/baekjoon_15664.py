import sys


def dfs(temp, start):
    if len(temp) == m:
        for i in temp:
            print(i, end=" ")
        print()
        return

    remember = 0
    for i in range(start, n):
        if remember != arr[i] and visited[i] == 0:
            temp.append(arr[i])
            visited[i] = 1
            remember = arr[i]
            dfs(temp, i+1)
            visited[i] = 0
            temp.pop()


n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
temp = []
visited = [0] * n

dfs(temp, 0)
