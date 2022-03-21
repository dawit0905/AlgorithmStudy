import sys


def dfs(array):
    if len(array) == m:
        for i in array:
            print(i, end=" ")
        print()
        return
    for i in range(n):
        if data[i] not in array:
            array.append(data[i])
            dfs(array)
            array.pop()

n, m = map(int ,sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
data.sort()
array = []

dfs(array)

