import sys


def dfs(start):
    if visited[start] == 1:
        return 0
    visited[start] = 1
    for i in cow_went[start]:
        if barn[i] == 0 or dfs(barn[i]):
            barn[i] = start
            return 1
    return 0


n, m = map(int, sys.stdin.readline().split())
cow_went = [[] for _ in range(n+1)]
barn = [0 for _ in range(m+1)]

for i in range(1, n+1):
    temp = list(map(int, sys.stdin.readline().split()))
    for j in temp[1:]:
        cow_went[i].append(j)

for i in range(1, n+1):
    visited = [0 for _ in range(n+1)]
    dfs(i)

print(len(barn) - barn.count(0))
