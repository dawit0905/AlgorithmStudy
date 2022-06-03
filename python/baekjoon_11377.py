import sys


def dfs(start):
    # 이미 매칭이 됐으면 리턴
    if visited[start] == 1:
        return 0
    visited[start] = 1
    # source가 할 수 있는 일들을 돌면서
    for i in s[start]:
        # 선택 되지 않은 일이나, 이미 선택한 source가 다른 일을 선택할 수 있으면
        if d[i] == 0 or dfs(d[i]):
            d[i] = start
            return 1
    return 0


n, m, k = map(int, sys.stdin.readline().split())
s = [[] for _ in range(n+1)]
d = [0 for _ in range(m+1)]
cnt = 0
for i in range(1, n+1):
    arr = list(map(int, sys.stdin.readline().split()))
    for j in arr[1:]:
        s[i].append(j)

for i in range(1, n+1):
    visited = [0 for _ in range(n+1)]
    if dfs(i):
        cnt += 1

for i in range(1, n+1):
    visited = [0 for _ in range(n+1)]
    if dfs(i):
        cnt += 1
        k -= 1
        if k == 0:
            break

print(cnt)

