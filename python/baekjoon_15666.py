import sys


def dfs(temp, num):
    if len(temp) == m:
        for i in temp:
            print(i, end=" ")
        print()
        return

    remember = 0
    for i in range(0, n):
        if remember != arr[i] and arr[i] >= num:
            temp.append(arr[i])

            remember = arr[i]
            dfs(temp, arr[i])

            temp.pop()


n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
temp = []
visited = [0] * n

dfs(temp, 0)
