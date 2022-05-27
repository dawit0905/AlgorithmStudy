import sys


def dfs(start):
    if visited[start] == 1:
        return 0
    visited[start] = 1
    for i in s[start]:
        if d[i] == 0 or dfs(d[i]):
            d[i] = start
            return 1
    return 0


t = int(sys.stdin.readline())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    # 백준이가 가지고 있는 책
    s = [[] for _ in range(m+1)]
    # 학생이 책을 받을 수 있는지 확인
    d = [0 for _ in range(n+1)]
    cnt = 0
    for i in range(1, m+1):
        a, b = map(int, sys.stdin.readline().split())
        for j in range(a, b+1):
            s[i].append(j)

    for i in range(1, m+1):
        visited = [0 for _ in range(m+1)]
        if dfs(i):
            cnt += 1

    print(cnt)
