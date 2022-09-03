import sys


def dfs(x):
    global result

    visited[x] = True
    cycle.append(x)

    if visited[arr[x]]:
        if arr[x] in cycle:
            result += cycle[cycle.index(arr[x]):]
        return
    else:
        dfs(arr[x])


sys.setrecursionlimit(10**5)
t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    arr = [0] + list(map(int, sys.stdin.readline().split()))
    result = []
    visited = [True] + [False] * n
    for i in range(1, n+1):
        if not visited[i]:
            cycle = []
            dfs(i)

    print(n - len(result))


