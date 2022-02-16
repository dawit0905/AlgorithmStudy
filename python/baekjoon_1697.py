from collections import deque


def bfs():
    que = deque()
    que.append(n)

    while que:
        x = que.popleft()
        if x == k:
            print(dist[x])
            break
        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx <= MAX and not dist[nx]:
                dist[nx] = dist[x] + 1
                que.append(nx)


n, k = map(int, input().split())
MAX = 10 ** 5
dist = [0] * (MAX + 1)
bfs()
