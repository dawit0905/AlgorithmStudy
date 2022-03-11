import sys
from collections import deque


def bfs():
    que = deque()
    que.append((1, 0))
    visited[1] = 1

    while que:
        num, cnt = que.popleft()

        if num == 100:
            return cnt

        for i in range(1, 7):
            next_num = num + i

            if next_num <= 100 and visited[next_num] == 0:
                # 이동할 위치에 사다리 있다면
                for start, end in arr:
                    if next_num == start:
                        next_num = end
                # 이동할 위치에 뱀이 있다면
                for start, end in arr2:
                    if next_num == start:
                        next_num = end
                # 이동할 위치에 사다리, 뱀이 없다면
                if visited[next_num] == 0:
                    visited[next_num] = 1
                    que.append((next_num, cnt+1))


n, m = map(int, sys.stdin.readline().split())
arr = []
arr2 = []
visited = [0] * 101

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    arr.append((a, b))

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    arr2.append((a, b))

print(bfs())
