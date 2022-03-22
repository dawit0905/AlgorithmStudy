import sys


def dfs(temp, index, num):
    if len(temp) == m:
        for i in range(m):
            print(temp[i], end=" ")
        print()
        return

    for i in range(index, n):
        if arr[i] not in temp:
            if arr[i] > num:
                temp.append(arr[i])
                dfs(temp, index+1, arr[i])
                temp.pop()


n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
temp = []

dfs(temp, 0, 0)
