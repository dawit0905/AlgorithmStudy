import sys


def dfs(start):
    if visited[start] == 1:
        return 0
    visited[start] = 1
    for i in can_do_it[start]:
        if work[i] == 0 or dfs(work[i]):
            work[i] = start
            return 1
    return 0


n, m = map(int, sys.stdin.readline().split())
can_do_it = [[] for _ in range(n+1)]
work = [0 for _ in range(m+1)]

for i in range(1, n+1):
    arr = list(map(int, sys.stdin.readline().split()))
    for j in arr[1:]:
        can_do_it[i].append(j)

for i in range(1, n+1):
    visited = [0 for _ in range(n+1)]
    dfs(i)

print(len(work) - work.count(0))

