import sys


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
   ap = find(parent, a)
   bp = find(parent, b)

   if ap < bp:
       parent[bp] = ap
   else:
       parent[ap] = bp


n, m = map(int, sys.stdin.readline().split())
parent = [i for i in range(n+1)]

edges = []
_sum = 0
for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    _sum += c
    edges.append((c, a, b))


edges.sort(key=lambda x: x[0])

answer = 0
line = 0
for cost, v, w in edges:
    if find(parent, v) != find(parent, w):
        union(parent, v, w)
        answer += cost
        line += 1

print(_sum - answer) if line == n-1 else print(-1)

