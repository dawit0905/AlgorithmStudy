import collections
import sys
from itertools import combinations
from collections import deque


def bfs(arr):
    start = arr[0]
    que = deque([start])
    visited = set([start])
    total = 0

    while que:
        now = que.popleft()
        total += distance[now]

        for i in edges[now]:
            if i not in visited and i in arr:
                que.append(i)
                visited.add(i)

    return total, len(visited)


n = int(sys.stdin.readline())
edges = collections.defaultdict(list)
distance = [0] + list(map(int, sys.stdin.readline().split()))
result = sys.maxsize

for i in range(1, n+1):
    arr = list(map(int, sys.stdin.readline().split()))
    for j in range(1, arr[0]+1):
        edges[i].append(arr[j])

for i in range(1, n//2+1):
    combis = list(combinations(range(1, n+1), i))
    for combi in combis:
        sum1, v1 = bfs(combi)
        sum2, v2 = bfs([i for i in range(1, n+1) if i not in combi])

        if v1 + v2 == n:
            result = min(result, abs(sum1-sum2))


if result != sys.maxsize:
    print(result)
else:
    print(-1)
