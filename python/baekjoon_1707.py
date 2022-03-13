from collections import deque
import sys


def bfs(start):
    visited[start] = 1
    q = deque()
    q.append(start)
    while q:
        a = q.popleft()
        for i in graph[a]:
            if visited[i] == 0:
                visited[i] = -visited[a]
                q.append(i)
            else:
                if visited[i] == visited[a]:
                    return False
    return True


k = int(input())
for i in range(k):
    v, e = map(int, sys.stdin.readline().split())
    flag = True
    graph = [[] for _ in range(v + 1)]
    visited = [0 for _ in range(v + 1)]
    for j in range(e):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    for k in range(1, v + 1):
        if visited[k] == 0:
            if not bfs(k):
                flag = False
                break
    print("YES"if flag else "NO")
