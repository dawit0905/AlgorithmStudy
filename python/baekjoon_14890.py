import sys


def move(now):
    for j in range(1, n):
        if abs(now[j] - now[j-1]) > 1:
            return False
        if now[j] < now[j-1]:
            for k in range(l):
                if j+k >= n or visited[j+k] or now[j] != now[j+k]:
                    return False
                if now[j] == now [j+k]:
                    visited[j+k] = 1
        elif now[j] > now[j-1]:
            for k in range(l):
                if j-k-1 < 0 or now[j-1] != now[j-k-1] or visited[j-k-1]:
                    return False
                if now[j-1] == now[j-k-1]:
                    visited[j-k-1] = 1
    return True


n, l = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

answer = 0
for i in range(n):
    visited = [0] * n
    if move(graph[i]):
        answer += 1

for i in range(n):
    visited = [0] * n
    if move([graph[j][i] for j in range(n)]):
        answer += 1

print(answer)